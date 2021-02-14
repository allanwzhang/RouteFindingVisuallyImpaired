# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:05:48 2021

@author: Jerry
"""

import csv
import numpy as np

def csvToArray(fileName):
    data = []
    with open(fileName, 'r') as csvfile:
        csvreader = csv.reader(csvfile) 
        for row in csvreader:
            data.append(row)
    return data

def writeCSV(data, fileName):
    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for ar in data:
            writer.writerow(ar)

data = csvToArray("filteredTree.csv")


write = []
for ar in data:
    currX = float(ar[0])
    currY = float(ar[1])
    currX -= 583739
    currY -= 4510607
    newX = currX*np.cos(np.deg2rad(28.35)) - currY*np.sin(np.deg2rad(28.35))
    newY = currX*np.sin(np.deg2rad(28.35)) + currY*np.cos(np.deg2rad(28.35))
    if newX >= 0 and newX <= 2475 and newY >= 0 and newY <= 3510:
        write.append([newX, newY])

writeCSV(write, "rectRotatedTree.csv")

'''
write = []
for ar in swData:
    a = ar[0]
    curr = a[1:-1].split(", ")
    if float(curr[0]) >= 0 and float(curr[0]) <= 2475 and float(curr[1]) >= 0 and float(curr[1]) <= 3510:
        write.append(ar)


writeCSV(write, "rectRotatedSidewalk.csv")

'''