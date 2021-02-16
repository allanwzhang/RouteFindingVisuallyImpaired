# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:01:41 2021

@author: Jerry
"""


import numpy as np
import matplotlib.pyplot as plt

graph = np.load("grid.npy")

x = np.empty(8000000)
y = np.empty(8000000)

index=0
for i in range(len(graph)):
    if graph[i] == 1:
        x[index] = i % 4950
        y[index] = int(i/4950)
        index+=1
print(index)

plt.scatter(x, y)
plt.show()