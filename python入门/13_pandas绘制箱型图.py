# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:34:02 2019

@author: Administrator
"""

import pandas as pd
scores =pd.read_excel('score.xlsx')
scores.boxplot()