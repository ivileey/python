# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:04:25 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0,4,0.1)
plt.plot(t,t,t,t+2,t,t**2)
plt.show()