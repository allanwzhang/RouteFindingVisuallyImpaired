# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 23:16:22 2021

@author: Jerry
"""

import csv
import numpy as np

def writeCSV(data, fileName):
    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for ar in data:
            writer.writerow(ar)
            
grid = np.load("cutGrid.npy")


write = []

for j in range(0, 630):
    arr = []
    for i in range(0, 1030):
        arr.append(int(grid[j*1030+i]))
    write.append(arr)
    
writeCSV(write, "cutGraph.csv")
'''
grid2 = np.empty(1030*630)
count=0
for j in range(5560, 6190):
    for i in range(3450, 4480):
        grid2[count] = int(grid[j*4950+i])
        count+=1

np.save("cutGrid.npy", grid2)
'''
