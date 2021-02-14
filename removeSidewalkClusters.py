# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:02:47 2021

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

treeData = csvToArray("filteredSidewalkRemovedCluster.csv")

'''
def parse(polygon):
    polygon = polygon[2:-3]
    stringcoords = polygon.split(")', '(")
    result = []
    for ar in stringcoords:
        curr = ar.split(", ")
        result.append(curr)
    
    return result

def dist(x, y):
    return np.sqrt((float(x[0])-float(y[0]))**2+(float(x[1])-float(y[1]))**2)

write = []
for ar in treeData:
    i = 0
    prev = len(ar)
    while i < len(ar)-1:
        coords1 = ar[i][1:-1].split(", ")
        coords2 = ar[i+1][1:-1].split(", ")
        if dist(coords1, coords2) < 0.2:
            ar.pop(i+1)
        else:
            i+=1
    write.append(ar)
    
writeCSV(write, "filteredSidewalkRemovedCluster.csv")

'''

write = []
for ar in treeData:
    new = []
    for c in ar:
        coords = c[1:-1].split(', ')
        currX = float(coords[0])
        currY = float(coords[1])
        currX -= 583739
        currY -= 4510607
        newX = currX*np.cos(np.deg2rad(28.35)) - currY*np.sin(np.deg2rad(28.35))
        newY = currX*np.sin(np.deg2rad(28.35)) + currY*np.cos(np.deg2rad(28.35))
        new.append([newX, newY])
    if len(write) == 55:
        print(new)
        break
    write.append(new)
#writeCSV(write, "rotatedSidewalk.csv")