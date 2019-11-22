import scipy.io as sio
import random
import numpy as np


def read(batch, data, is_training=True):
    if is_training:
        np.random.shuffle(data)
    for i in range(len(data)):
        batch_data = data[i*batch:(i+1)*batch]
        img = batch_data[:, 1:].reshape(batch, -1, 1)
        label = batch_data[:, 0]
        label = label - 1
        yield img, label.astype(np.int64)


if __name__=="__main__":
    data = sio.loadmat('data_cls_3.mat')
    train = data['train']
    test = data['test']
    train_gen = read(27, train)
    ll = []
    for i in range(31):
        train_data, train_label = train_gen.__next__()
        ll.extend(train_label)
    print('-')