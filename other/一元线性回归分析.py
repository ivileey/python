# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:31:21 2019

@author: Administrator
"""

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

clf =linear_model.LinearRegression()
X = np.array([2,3,5,7,6]).reshape(-1,1)
Y = np.array([6,10,14.5,21,18.5])
clf.fit(X,Y)
b, a = clf.coef_,clf.intercept_
print(b,a)
x = [[4]]
print(clf.predict(x))
plt.plot(X,a+b*X,color='red')