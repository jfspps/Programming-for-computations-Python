# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 22:14:57 2020

@author: James Apps
"""

import matplotlib.pyplot as plt
from math import exp

List_1 = []
for i in range(-20, 20, 1):
    List_1.append(i)

List_2 = [exp(e)-e**3 for e in List_1]

plt.plot(List_1, List_2)
plt.xlabel('x')
plt.ylabel('exp(x) - x^3')
plt.show

#save to binary file
filename = 'coords.dat'
outfile = open(filename, 'w')
outfile.write('Here are the x and y values:\n')
for x, y in zip(List_1, List_2):
    outfile.write('%3.3f %3.3f\n' % (x, y))
outfile.close

#extract every other pair of coords
infile = open(filename, 'r')
print infile.readline()
switch = True
for line in infile:
    words = line.split()
    if switch:
        print 'x = ', words[0], '\ty = ', words[1]
        switch = False
    else:
        switch = True
infile.close()

        
        
        