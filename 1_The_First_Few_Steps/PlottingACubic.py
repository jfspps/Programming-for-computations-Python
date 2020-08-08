# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:24:04 2020

@author: apps_
"""


import matplotlib.pyplot as plt
from numpy import zeros
from numpy import linspace

L = linspace(1,3,3)
v = zeros(3)
v[0] = L[0]**3
v[1] = L[1]**3
v[2] = L[2]**3
V = L**3

for i in range(3):
        print(v[i])

plt.plot(L, V)
plt.xlabel('cube length L')
plt.ylabel('cube volume V')