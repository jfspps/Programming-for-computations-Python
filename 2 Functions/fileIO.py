# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:18:18 2020

@author: apps_
"""


filename = 'tmp.dat'
infile = open(filename, 'r')
line = infile.readline()

x = []
y = []

for line in infile:
    #create an array of string
    words = line.split()
    x.append(float(words[0]))
    y.append(float(words[1]))
infile.close()

#transform the coords
from math import log

def f(y):
    return log(y)

#save lof y coords in the array y
for i in range(len(y)):
    y[i] = f(y[i])
    
filename='temp_out.dat'
outfile = open(filename, 'w')
outfile.write('# x and y coordinates\n')
#zip is a function which processes two lists at the same time
for xi, yi in zip(x, y):
    outfile.write('%10.5f %10.5f\n' % (xi, yi))
outfile.close()

import matplotlib.pyplot as plt
plt.plot(x, y, 4)
plt.show()