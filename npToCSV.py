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
            
grid = np.load("grid.npy")

write = []

for i in range(3450, 4480):
    arr = []
    for j in range(5560, 6190):
        arr.append(int(grid[j*4950+i]))
    write.append(arr)

writeCSV(write, "cutGraph.csv")