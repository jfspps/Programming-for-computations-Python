# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:21:49 2020

@author: James Apps
"""

from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

#note that y is an array

largest_height = y[0]
#range is zero based; two arguments assumes a step size of 1
for i in range(1, 1000):
    if y[i] > largest_height:
        largest_height = y[i]

print "The largest height achieved was %f m" %(largest_height)

plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

#using for loops in summations
N = 5
x = 0
for i in range(1, N+1):
    x += 2*i
print x