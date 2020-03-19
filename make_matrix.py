#!/usr/bin/python3
import sys
import random
import csv

lst = []
with open('matrix50kX50k.csv', 'w') as csvFile:
 for j in range(50000):
  innerList = []
  for i in range(50000):
   innerList.append(random.randint(0,50000))
  writer = csv.writer(csvFile,delimiter=' ')
  writer.writerow(innerList)
csvFile.close()


print("Export complete")

