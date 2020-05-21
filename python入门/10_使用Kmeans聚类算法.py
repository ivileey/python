# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:55:24 2019

@author: Administrator
"""

import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten

list1=[88.0,74.0,96.0,85.0]
list2=[92.0,99.0,95.0,94.0]
list3=[91.0,87.0,99.0,95.0]
list4=[78.0,99.0,97.0,81.0]
list5=[88.0,78.0,98.0,84.0]
list6=[100.0,95.0,100.0,92.0]
list7=[100.0,98.0,99.0,97.0,]

allList = np.array([list1,list2,list3,list4,list5,list6,list7])
whiten = whiten(allList)
a,_= kmeans(whiten,3)
print(a)
result,_=vq(whiten,a)
print(result)