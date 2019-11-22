import os
from glob import glob
import numpy as np
import pandas as pd
import random
import scipy.io as sio
import matplotlib.pyplot as plt


def readtxt(txt_path, label_numpy):
    train_data = np.array([])
    test_data = np.array([])
    for txt in txt_path:
        name = int(txt.split('\\')[-1][-11])
        label = label_numpy[name - 1]
        single_char = [line.strip().split(' ') for i, line in enumerate(open(txt, 'r')) if i > 0]
        single_float = np.array([])
        for line in single_char:
            single_float = np.r_[single_float, [float(ch) for ch in line]]
        single_float = single_float.reshape(-1, 4).transpose()
        single_label = np.tile(label, 4)
        single_data = np.c_[single_label, single_float]
        np.random.shuffle(single_data)
        if train_data.any():
            train_data = np.r_[train_data, single_data]
            test_data = np.r_[test_data, single_data[3:, :]]
        else:
            train_data = single_data[:3, :]
            test_data = single_data[3:, :]
    return train_data, test_data


'''
def readtxt(txt_path, label_numpy):
    train_data = np.array([])
    test_data = np.array([])
    for txt in txt_path:
        name = int(txt.split('\\')[-1][-11])
        label = label_numpy[name-1]
        single_char = [line.strip().split(' ') for i, line in enumerate(open(txt, 'r')) if i>0]
        single_float = np.array([])
        for line in single_char:
            single_float = np.r_[single_float, [float(ch) for ch in line]]
        single_float = single_float.reshape(-1, 4).transpose()
        # single_float = single_float.reshape(4, 2, 2500)
        # single_float_tra = single_float[:, :1, :].reshape(-1, 2500)
        # single_float_tes = single_float[:, 1:, :].reshape(-1, 2500)
        single_float_tra = single_float[:, ::2]
        single_float_tes = single_float[:, 1::2]
        single_float_tra = np.c_[np.tile(label, 4), single_float_tra]
        single_float_tes = np.c_[np.tile(label, 4), single_float_tes]
        if train_data.any():
            train_data = np.r_[train_data, single_float_tra]
            test_data = np.r_[test_data, single_float_tes]
        else:
            train_data = single_float_tra
            test_data = single_float_tes
    return train_data, test_data
'''


path_csv = 'C:\\Users\\sk\\Desktop\\33\\class.xlsx'
path = 'C:\\Users\\sk\\Desktop\\33\\33\\33_result' # C:\Users\sk\Desktop\33\33\33_result

df = pd.read_excel(path_csv)
label_numpy_3 = df.values[:, 1]  # 3分类标签
label_numpy_6 = df.values[:, 2]  # 6分类标签

train_data = np.array([])
test_data = np.array([])
for file_path in glob(os.path.join(path, '*')):
    txt_path = glob(os.path.join(file_path, '*-1_out.txt'))
    train_file, test_file = readtxt(txt_path, label_numpy_6)
    print(file_path.split('\\')[-1], 'txt_path:', len(txt_path), 'train_file:', len(train_file), 'test_file:', len(test_file))
    if train_data.any():
        train_data = np.r_[train_data, train_file]
        test_data = np.r_[test_data, test_file]
    else:
        train_data = train_file
        test_data = test_file
sio.savemat('data/data_cls_6.mat', {'train': train_data, 'test': test_data})
