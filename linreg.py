# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:00:14 2016

@author: laura
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = [1.0 / 0.05, 1.0 / 0.15, 1.0 / 0.26, 1.0 / 0.35]
y = [1.0 / 1.4, 1.0 / 3.6, 1.0 / 5.5, 1.0 / 6.8]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

t = np.linspace(0, 10, 10)
f = slope * t + intercept

plt.plot(t, f)
plt.plot(x, y, '.')
plt.show()

print stats.linregress(x,y)
