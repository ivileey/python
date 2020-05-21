# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:18:56 2019

@author: Administrator
"""

from sklearn import cluster,datasets
iris = datasets.load_iris()
kmeans=cluster.KMeans(n_clusters=3).fit(iris.data)
pred=kmeans.predict(iris.data) #确定数据类别

for label in pred:
    print(label,end='')#打印预测出的各条数据的标签
print('\n')
for label in iris.target:
    print(label,end = '') #打印原始标注好的正确标签