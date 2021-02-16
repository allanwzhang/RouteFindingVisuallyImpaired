# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:52:14 2021

@author: Jerry
"""

import utm
import numpy as np

t = utm.from_latlon(40.7572180168, -73.9861957434)
xy = [t[0], t[1]]

xy[0] -= 583739
xy[1] -= 4510607
newX = xy[0]*np.cos(np.deg2rad(28.35)) - xy[1]*np.sin(np.deg2rad(28.35))
newY = xy[0]*np.sin(np.deg2rad(28.35)) + xy[1]*np.cos(np.deg2rad(28.35))

def findIndex(x,y):
    return int(4950*np.round(y*2)+np.round(x*2))

index = findIndex(newX, newY)
print(index)

grid = np.load("grid.npy")
print(grid[index])