# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:00:08 2021

@author: Jerry
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

graph = csvToArray("C:\Allan\intermediate\\showNearest.csv")

values = np.empty(67160)

index = 0
for j in range(400, 630):
    for i in range(300, 592):    
        values[index] = graph[j*1030+i]
        index+=1
print(index)

xygraph = np.reshape(values, (-1, 292))


#print(xygraph[626])
for i in range(224, 230):
    for j in range(0, 292):
        xygraph[i][j]=6


ax = sns.heatmap(xygraph)
ax.invert_yaxis()