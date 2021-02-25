# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:34:26 2021

@author: Jerry
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

def csvToArray(fileName):
    data = np.empty(630*1030)
    i = 0
    with open(fileName, 'r') as csvfile:
        csvreader = csv.reader(csvfile) 
        for row in csvreader:
            for x in row:
                data[i] = x
                i+=1
    return data

graph = csvToArray("C:\Allan\intermediate\\testGraph.csv")

x = np.empty(73896)
y = np.empty(73896)

index = 0
for i in range(0, 1030):
    for j in range(0, 630):
        if graph[j*1030+i] == 0:
            x[index] = i
            y[index] = j
            index+=1
print(index)

plt.scatter(x, y)
plt.show()

