# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:22:34 2019

@author: Administrator
"""

#随机函数产生500行1-100的数字存入文件中寻找众数

import random
with open('random.txt','w+') as f:
    for i in range(500):
        f.write(str(random.randint(1,100)))
        f.write('\n')
    f.seek(0)
    nums=f.readlines()
nums=[num.strip() for num in nums]
setNums=set(nums)
lst=[0]*101
for num in setNums:
    c=nums.count(num)
    lst[int(num)]=c
for i in range(len(lst)):
    if lst[i]==max(lst):
        print(i)
    