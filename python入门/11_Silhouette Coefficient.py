# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:36:26 2019

@author: Administrator
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics

iris = datasets.load_iris()
X = iris.data

K = range(2,9)
lst = []
for k in K :
    kmeans_model = KMeans(n_clusters = k).fit(X)
    sc_score = metrics.silhouette_score(X,kmeans_model.labels_,metric = 'euclidean')
    lst.append(sc_score)
plt.plot(K,lst,'bo-')
plt.title('Silhouette Coefficient')
plt.xlabel("K")
plt.ylabel("Score")
plt.show()