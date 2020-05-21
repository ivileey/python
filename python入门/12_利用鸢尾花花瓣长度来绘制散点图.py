# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:23:08 2019

@author: Administrator
"""

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X=[item[0] for item in iris.data]
Y=[item[2] for item in iris.data]
plt.scatter(X[:50],Y[:50],color='red',marker='o',label='setosa')
plt.scatter(X[50:100],Y[50:100],color = 'green',marker='*',label='versicolor')
plt.scatter(X[100:],Y[100:],color='blue',marker='D',label='virginca')
plt.legend(loc='best')