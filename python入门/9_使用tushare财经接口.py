# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:14:45 2019

@author: Administrator
"""

import tushare as ts
import numpy as np
df=ts.get_hist_data('600036',start='2018-07-01',end='2018-12-31')
df=df.iloc[:,:5]
df.sort_index(inplace=True)
min_day = df.sort_values('volume').iloc[0,]
min_volume = min_day.volume
min_volume_date = min_day.name
print("the min volume is {} at {}".format(min_volume,min_volume_date))
max_day = df.sort_values('volume').iloc[-1,]
max_volume = max_day.volume
max_volume_date = max_day.name
print("the max volume is {} at {}".format(max_volume,max_volume_date))

#print(df[df.volume>=1000000])

#print(len(df[df.close>df.open]))

#print(df.open.diff())
print(np.sign(np.diff(df.open)))
#print(df)

month = [item[5:7] for item in df.index]
print(df.close.groupby(month).apply(np.mean))