# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:12:53 2019

@author: Administrator
"""

from sklearn import neighbors,datasets
iris = datasets.load_iris()
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data,iris.target)
p=knn.predict([[5.0,3.0,5.0,2.0]])
print(p)