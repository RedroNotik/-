# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:47:00 2021

@author: timof
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.fromfile('x_data.txt', float, sep = '\n')
y = np.fromfile('y_data.txt', float, sep = '\n')


n = len(x)
a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x*x) - np.sum(x) * np.sum(x))
b = (np.sum(y) - a * np.sum(x))/(n)

yansw = a*x + b
print(yansw, a, b)

plt.scatter(x, y)
plt.plot(x,yansw)
plt.show()