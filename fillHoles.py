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
graph[300*1030+623]=1
graph[189*1030+623]=1
graph[308*1030+939]=1
graph[169*1030+701]=1
graph[178*1030+904]=1
graph[177*1030+964]=1
graph[177*1030+918]=1
graph[177*1030+928]=1
graph[139*1030+24]=1
graph[459*1030+14]=1
graph[465*1030+20]=1
graph[465*1030+114]=1
graph[328*1030+1011]=1


x = np.empty(2066)
y = np.empty(2066)

#1030: 0, 280, 600, 1030
#630: 0, 310, 480, 630

#0-280, 280-600, 600-1030 (480-630)

index = 0
for i in range(600, 1030):
    for j in range(310, 480):
        if graph[j*1030+i] == 1:
            x[index] = i
            y[index] = j
            index+=1
print(index)

plt.scatter(x, y)
plt.show()

np.save("cutGrid.npy", graph)