# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:19:50 2019

@author: Administrator
"""

from sklearn import datasets
import matplotlib.pyplot as plt
boston = datasets.load_boston();
X = boston.data;
Y = boston.target;
print(X.shape)
print(boston)
#plt.scatter(X['RM'],Y,color='blue')
#plt.scatter(X['LSTAT'],Y,color='blue')