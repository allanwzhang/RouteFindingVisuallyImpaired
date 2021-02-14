# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:09:16 2021

@author: Jerry
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def csvToArray(fileName):
    data = []
    with open(fileName, 'r') as csvfile:
        csvreader = csv.reader(csvfile) 
        for row in csvreader:
            data.append(row)
    return data


swData = csvToArray("rectRotatedSidewalk.csv")

x = np.empty(128517)
y = np.empty(128517)

i=0
for ar in swData:
    for a in ar:
        curr = a[1:-1].split(", ")
        x[i] = float(curr[0])
        y[i] = float(curr[1])
        i+=1
print(i)
'''
i=0
for ar in swData:
    x[i] = ar[0]
    y[i] = ar[1]
    i+=1
print(i)
'''
plt.scatter(x, y)
plt.show()