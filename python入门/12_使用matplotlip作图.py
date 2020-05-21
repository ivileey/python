# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:13:18 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,500)
y1 = np.sin(x)
y2 = np.sin(x*3)

fig,ax = plt.subplots()
ax.fill(x, y1, 'b', x, y2, 'r',alpha=0.3)
plt.show()