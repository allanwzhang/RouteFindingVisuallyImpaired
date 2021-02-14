# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:31:49 2021

@author: Jerry
"""

#Bottom Left: 583383, 4509216
#Top Right: 588001, 4513961

import utm
import csv
import sys

maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
csv.field_size_limit(maxInt)

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
            
            
treeData = csvToArray("SIDEWALK.csv")

print(treeData[0])

def parse(polygon):
    polygon = polygon[16:-3]
    stringcoords = polygon.split(", ")
    result = []
    for ar in stringcoords:
        curr = ar.split(" ")
        if curr[0][0] == "(":
            curr[0] = curr[0][1:]
        if curr[1][-1] == ")":
            curr[1] = curr[1][:-1]
        result.append(utm.from_latlon(float(curr[1]), float(curr[0]))[0:2])
    return result

print(len(treeData))


count = 0
write = []
first = True
for ar in treeData:
    count += 1
    if count % 10000 == 0:
        print(count)
    if first:
        first = False
        continue
    parsed = parse(ar[0])
    if parsed[0][0] < 583383 or parsed[0][0] > 588001 or parsed[0][1] < 4509216 or parsed[1][1] > 4513961:
        continue
    write.append(parsed)

writeCSV(write, "filteredSidewalk.csv")
