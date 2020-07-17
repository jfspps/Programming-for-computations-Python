#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 01:06:13 2020

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt

print("Linear interpolation example")
print("============================")

def findY(y, t):
    if t in range(len(y)):
        print("Linear interpolation not required")
        return y[t]
    else:
        print("Linear interpolation proceeding...")
        low = int(t)
        high = low + 1
        yMid = (y[high] - y[low])*(t - low) + y[low]
        return yMid

def enterPairs(N):
    y = np.zeros(N+1)
    time = 0
    while time >= 0:
        time = int(input("Enter a time period in whole min: "))
        print("Time t = ", time)
        if time >=0:
            temp = float(input("Enter a y-value at time t: "))
            y[time] = temp
    return y

def maxTime():
    max = int(input("Enter the time interval N:\n"))
    return enterPairs(max)

# =============================================================================
# #User input verified
#
# output = maxTime()
# 
# print(output)
# 
# print(findY(output, 0.5))
# =============================================================================

y = [4.4, 2.0, 11.0, 21.5, 7.5]
ind = np.linspace(0, len(y)-1, len(y))

print(findY(y, 2.1), "\n")

print(findY(y, 4), "\n")

plt.plot(ind, y)
plt.xlabel('time t')
plt.ylabel('y')
plt.show()

