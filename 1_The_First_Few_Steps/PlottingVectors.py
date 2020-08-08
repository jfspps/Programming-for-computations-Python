# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:35:01 2020

@author: apps_
"""


from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = linspace(0, 1, 1001)

#y is now a vector
y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()