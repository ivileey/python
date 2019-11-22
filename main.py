import tensorflow as tf
import os
import numpy as np
import scipy.io as sio
import data_gen
import matplotlib.pyplot as plt


class electModel():
    def __init__(self, gpu=False, lr=1e-5, cls=3, checkpoint_dir='./model', model_name='./weakTest1'):
        self.cls = cls
        self.checkpoint_dir = checkpoint_dir
        self.model_name = model_name
        self.lr = lr
        # 参数初始化
        self.inputs = None
        self.labels = None
        self.is_training = None
        self.out = None
        self.accr = None
        self.loss = None
        self.optm = None
        self.saver = None

        if gpu:
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.Session(config=config)
        else:
            self.sess = tf.Session()
        self.build()

    def inference(self, inputs):
        with tf.variable_scope("conv1"):
            net = tf.layers.conv1d(inputs, 32, 7, strides=3, padding='same', activation=tf.nn.relu)
        with tf.name_scope("pool1"):
            net = tf.nn.pool(net, window_shape=[2], strides=[2], pooling_type="MAX", padding='SAME')
        with tf.variable_scope("conv2"):
            net = tf.layers.conv1d(net, 32, 7, strides=1, padding='same', activation=tf.nn.relu)
        with tf.name_scope("pool2"):
            net = tf.nn.pool(net, window_shape=[2], strides=[2], pooling_type="MAX", padding='SAME')
        with tf.variable_scope("conv3"):
            net = tf.layers.conv1d(net, 32, 7, strides=1, padding='same', activation=tf.nn.relu)
        with tf.name_scope("pool3"):
            net = tf.nn.pool(net, window_shape=[2], strides=[2], pooling_type="MAX", padding='SAME')
        with tf.variable_scope("fc1"):
            shape = net.get_shape().as_list()
            net = tf.reshape(net, [-1, shape[1] * shape[2]])
            net = tf.layers.dense(net, 512, activation=tf.nn.relu)
        with tf.variable_scope("fc2"):
            net = tf.layers.dropout(net, training=self.is_training)
            net = tf.layers.dense(net, self.cls)
        return net

    def build(self):
        self.inputs = tf.placeholder(tf.float32, [None, 5000, 1], "inputs")
        self.labels = tf.placeholder(tf.int64, [None], "labels")
        self.is_training = tf.placeholder(tf.bool, name="is_training")
        with tf.name_scope("outputs"):
            self.out = self.inference(self.inputs)
        with tf.name_scope("accr"):
            self.accr = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(self.out, 1), self.labels), tf.float32))
        with tf.name_scope("loss"):
            self.loss = tf.reduce_mean(
                tf.nn.sparse_softmax_cross_entropy_with_logits(logits=self.out, labels=self.labels))
        with tf.name_scope("optm"):
            self.optm = tf.train.AdamOptimizer(self.lr).minimize(self.loss)
        # 模型保存
        self.saver = tf.train.Saver(max_to_keep=2)
        # 初始化
        init = tf.global_variables_initializer()
        self.sess.run(init)

    def train(self, nEpochs=30, batchsize=32, display=20):
        # 检测是否有保存的模型
        if self.load(self.checkpoint_dir):
            print(" [*] Load SUCCESS")
        else:
            print(" [!] Load failed...")
        # 数据读取
        data = sio.loadmat('data/data_cls_3.mat')
        train = data['train']
        test = data['test']
        # 开始训练
        epochSize = int(len(train) / batchsize)
        validIter = int(len(test) / 31)
        ac = []
        co = []
        for epoch in range(nEpochs):
            genrator_train = data_gen.read(batchsize, train)
            genrator_test = data_gen.read(31, test, False)
            avg_train_cost = 0.
            avg_train_accr = 0.
            avg_val_accr = 0.
            avg_val_cost = 0.
            print('Epoch :' + str(epoch) + '/' + str(nEpochs))
            # 训练
            for i in range(epochSize):
                img_train, label_train = next(genrator_train)
                _, c, accr_train = self.sess.run([self.optm, self.loss, self.accr], feed_dict={self.inputs: img_train,
                                                                                               self.labels: label_train,
                                                                                               self.is_training: True})
                avg_train_cost += c / epochSize
                avg_train_accr += accr_train / epochSize
                if i % display == 0:
                    print("epoch/batch_epoch:%d/%d loss:%f accr:%f" % (epoch, i, c, accr_train))
            # 测试
            for _ in range(validIter):
                img_valid, label_valid = next(genrator_test)
                cv, accr_val = self.sess.run([self.loss, self.accr],
                                             feed_dict={self.inputs: img_valid,
                                                        self.labels: label_valid,
                                                        self.is_training: False})
                avg_val_cost += cv / validIter
                avg_val_accr += accr_val / validIter
            # 保存模型
            # self.save(self.checkpoint_dir, epoch)
            print("avg_train_loss:%f avg_train_accr:%f" % (avg_train_cost, avg_train_accr))
            print("avg_val_loss:%f avg_val_accr:%f" % (avg_val_cost, avg_val_accr))
            ac.append(avg_val_accr)
            co.append(avg_val_cost)
        # sio.savemat('log/log6.mat', {'accr': ac, 'loss': co})


    def predict(self, num):
        # 检测是否有保存的模型
        if self.load(self.checkpoint_dir):
            print(" [*] Load SUCCESS")
        else:
            print(" [!] Load failed...")
        # 数据读取
        data = sio.loadmat('data/data_cls_3.mat')
        test = data['test']
        # 开始训练
        generator = data_gen.read(31, test, False)
        mean_accr = []
        for _ in range(num):
            img, label = next(generator)
            out, loss, accr = self.sess.run([tf.argmax(self.out, 1), self.loss, self.accr],
                                            feed_dict={self.inputs: img,
                                                       self.labels: label,
                                                       self.is_training: False})
            print(out)
            print(label)
            # print(loss)
            print(accr)
            mean_accr.append(accr)
        print('The mean accuracy:', np.array(mean_accr).mean())

    def save(self, checkpoint_dir, step):
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
        self.saver.save(self.sess, os.path.join(
            checkpoint_dir, self.model_name), global_step=step)

    def load(self, checkpoint_dir):
        print(" [*] Reading checkpoint...")
        ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
        if ckpt and ckpt.model_checkpoint_path:
            ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
            self.saver.restore(self.sess, os.path.join(
                checkpoint_dir, ckpt_name))
            return True
        else:
            return False


if __name__ == "__main__":
    want = 0
    model = electModel(gpu=1, lr=1e-4, cls=3, checkpoint_dir='./model3',
                       model_name='softness')
    if want:
        model.train(nEpochs=20)
    else:
        model.predict(9)
