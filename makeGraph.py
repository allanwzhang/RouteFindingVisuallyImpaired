# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:17:26 2021

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

def findIndex(x,y):
    return int(4950*np.round(y*2)+np.round(x*2))

def fillGrid(data, size, indic):
    for ar in data:
        x = float(ar[0])
        y = float(ar[1])
        for i in range(-1 * size, size + 1):
            for j in range(-1 * size, size + 1):
                index = findIndex(x+i/2,y+j/2)
                if index < len(grid):
                    grid[index] = indic        

'''        
grid = np.empty(4950*7020)

tree = csvToArray("rectRotatedTree.csv")
hydrant = csvToArray("rectRotatedHydrant.csv")
shelter = csvToArray("rectRotatedBusShelter.csv")
newsstand = csvToArray("rectRotatedNewsstand.csv")
subway = csvToArray("rectRotatedSubwayEntrance.csv")

#Blank = 0
#Sidewalk = 1
#Obstacle = 2
#Ramp = 3

fillGrid(tree, 3, 2)
fillGrid(hydrant, 1, 2)
fillGrid(shelter, 3, 2)
fillGrid(newsstand, 3, 2)
fillGrid(subway, 5, 2)
'''

grid = np.load("grid.npy")
swData = csvToArray("rectRotatedSidewalk.csv")

def bresenham(x1, y1, x2, y2):
    flip = abs(y2-y1) > abs(x2-x1)
    if flip:
        tmp = x1
        x1 = y1
        y1 = tmp
        tmp = x2
        x2 = y2
        y2 = tmp
    derr = abs(y2-y1)
    yStep = 1
    if y2 < y1:
        yStep = -1
    dx = x2-x1
    err = dx>>1
    y = y1
    for x in range(x1, x2+1):
        if flip:
            grid[x*4950+y] = 1
        else:
            grid[y*4950+x] = 1
        err -= derr
        if err < 0:
            y += yStep
            err += dx

for ar in swData:
    for i in range(len(ar)-1):
        curr = ar[i][1:-1].split(", ")
        adj = ar[i+1][1:-1].split(", ")
        currX = float(curr[0])
        currY = float(curr[1])
        adjX = float(adj[0])
        adjY = float(adj[1])
        d = np.sqrt((currX-adjX)**2+(currY-adjY)**2)
        if(d < 1):
            grid[findIndex(currX, currY)] = 1
            grid[findIndex(adjX, adjY)] = 1
        else:
            ci = findIndex(currX, currY)
            ai = findIndex(adjX, adjY)
            if ci%4950 == ai%4950:
                minY = min(int(ci/4950), int(ai/4950))
                maxY = max(int(ci/4950), int(ai/4950))
                for j in range(minY, maxY+1):
                    grid[ci%4950+j*4950] = 1
            elif int(ci/4950)==int(ai/4950):
                minY = min(int(ci%4950), int(ai%4950))
                maxY = max(int(ci%4950), int(ai%4950))
                for j in range(minY, maxY+1):
                    grid[j+int(ci/4950)*4950] = 1
            else:
                if ci%4950 < ai%4950:
                    bresenham(ci%4950, int(ci/4950), ai%4950, int(ai/4950))
                else:
                    bresenham(ai%4950, int(ai/4950), ci%4950, int(ci/4950))

ramp = csvToArray("rectRotatedRamp.csv")
fillGrid(ramp, 0, 3)
np.save("grid.npy", grid)
