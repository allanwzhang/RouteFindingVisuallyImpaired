# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:01:41 2021

@author: Jerry
"""


import numpy as np
import matplotlib.pyplot as plt

graph = np.load("grid.npy")

x = np.empty(20800)
y = np.empty(20800)
'''
index=0
for i in range(len(graph)):
    if graph[i] == 1:
        x[index] = i % 4950
        y[index] = int(i/4950)
        index+=1
print(index)
'''
#3450, 4480
#5560, 6190
index = 0
for i in range(3450, 4480):
    for j in range(5560, 6190):
        if graph[j*4950+i] == 1:
            x[index] = i
            y[index] = j
            index+=1
            #print(i,j)
print(index)

plt.scatter(x, y)
plt.show()