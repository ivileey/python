# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:27:51 2019

@author: Administrator
"""

from sklearn import svm,datasets
iris = datasets.load_iris()
svc = svm.LinearSVC()
svc.fit(iris.data,iris.target)#学习
print(svc.predict([[5.0,3.0,5.0,2.0]]))