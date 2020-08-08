#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:27:50 2020

@author: james
"""

import matplotlib.pyplot as plt
import numpy as np

def lin(t, a, b):
    return a*t + b


#Fitting straight line data (x and y are lists)
def fit(x, y):
    a = float(input("Enter a value for a: "))
    b = float(input("Enter b value for b: "))
    err = 0
    plt.xlabel('x')
    plt.ylabel('ax + b')
    
    #compute the error err
    for i in range(len(x)):
        err = err + (lin(x[i],a,b) - dataPoints[i])**2
    
    #pass a list and return a list
    y = []
    for i in range(len(x)):
        y.append(lin(x[i],2,3))
    
    #plot two sets of data; x and dataPoints are given *
    plt.plot(x, y, x, dataPoints, '*')
    print("x[", i, "] =", x[i], ", y[", i, "] =", y[i])
    
    print("error = ", err)
    plt.show()
    return err

x = [0, 1, 2, 3, 4]
dataPoints = [0.5, 2.0, 1.0, 1.5, 7.5]

fit(x, dataPoints)