# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:08:59 2021

@author: Jerry
"""

import numpy as np
import matplotlib.pyplot as plt

graph = np.load("cutGrid.npy")

graph[7*1030+44]=1
graph[148*1030+21]=1
graph[147*1030+313]=1
graph[148*1030+313]=1
graph[32*1030+582]=1
graph[8*1030+892]=1
graph[17*1030+967]=1
graph[307*1030+178]=1
graph[299*1030+178]=1
graph[307*1030+20]=1
graph[307*1030+407]=1
graph[257*1030+316]=1
graph[169*1030+514]=1

x = np.empty(2064)
y = np.empty(2064)

#1030
#630

index = 0
for i in range(600, 1030):
    for j in range(160, 310):
        if graph[j*1030+i] == 1:
            x[index] = i
            y[index] = j
            index+=1
print(index)

plt.scatter(x, y)
plt.show()

np.save("cutGrid.npy", graph)