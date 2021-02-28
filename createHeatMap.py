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
xygraph = np.reshape(graph, (-1, 1030))
#print(xygraph[626])
for i in range(625, 630):
    for j in range(0, 1030):
        xygraph[i][j]=15

ax = sns.heatmap(xygraph)
ax.invert_yaxis()