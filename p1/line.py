#coding=utf-8
'''
Created on 2018年7月27日

@author: zhaoqinghua
'''

import numpy as np
import matplotlib.pyplot as plt

# ax = plt.gca()
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))
# ax.spines['right'].

x = np.linspace(-10, 10, 1000)
y = x * 3
# plt.figure()
plt.plot(x, y)
# plt.show()

y = x * 5
# plt.figure()
plt.plot(x, y)
plt.show()