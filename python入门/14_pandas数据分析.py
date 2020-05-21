# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:04:09 2019

@author: Administrator
"""

import pandas as pd
Singer=[('the rolling','Beatles','Guns','Metallica'),('Satisfaction','Let it be','Dont cry','Nothing else matters')]
a=pd.DataFrame(Singer)
print(a)
a.to_csv('sing.csv')