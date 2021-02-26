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

#22562
x = np.empty(22562)
y = np.empty(22562)

index = 0
for i in range(0, 1030):
    for j in range(0, 630):
        if graph[j*1030+i] == 1:
            x[index] = i
            y[index] = j
            index+=1
print(index)

plt.scatter(x, y)

#2198
x2 = np.empty(2198)
y2 = np.empty(2198)

index = 0
for i in range(0, 1030):
    for j in range(0, 630):
        if graph[j*1030+i] == 2:
            x2[index] = i
            y2[index] = j
            index+=1
print(index)

plt.scatter(x2, y2)

fileName = "C:\Allan\intermediate\Path.csv"

x3 = np.empty(1603)
y3 = np.empty(1603)

i=0
with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile) 
    for row in csvreader:
        x3[i] = row[0]
        y3[i] = row[1]
        i += 1
print(i)

plt.scatter(x3, y3)

plt.show()
