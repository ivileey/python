# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:22:45 2019

@author: Administrator
"""
# 未完成

import pandas as pd
from scipy.interpolate import lagrange #导入拉格朗日插值函数

df =pd.read_excel("nan.xlsx")
for i in df.columns:
    for j in range(len(df)):
        if(df[i].isnull())[j]:
            k=3
            y=df[i]