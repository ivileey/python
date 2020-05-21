# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:35:20 2019

@author: Administrator
"""

#利用肘方法确定Kmeans算法的K值
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

iris = datasets.load_iris()
X = iris.data
K=range(1,9)
lst=[]
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    lst.append(sum(np.min(cdist(X,kmeans.cluster_centers_,'euclidean'),axis=1))/X.shape[0])
plt.plot(K,lst,'bo-')
plt.title('Elbow method')
plt.xlabel("K")
plt.ylabel("Cost function")
plt.show()