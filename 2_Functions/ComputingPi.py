#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:29:49 2020

@author: james
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def denominator(k):
    return (4*k + 1) * (4*k + 3)

def denominator2(k):
    return k**2

# Leibniz form to compute Pi
def Leibniz(N, arr = []):
    temp = 0.0
    for i in range(0, N-1):
        temp += (1.0 / denominator(i))
        arr[i] = math.pi - 8 * temp
    return 8 * temp

# Euler form to compute Pi
def Euler(N, arr = []):
    temp = 0.0
    for j in range(1, N):
        temp += (1.0 / denominator2(j))
        arr[j-1] = math.pi - math.sqrt(6 * temp)
    return math.sqrt(6 * temp)

# Python 3 input() returns a string so cast int()
a = int(input('Enter the number of terms: '))

# array of zeros
LeibnizError = np.zeros(a)
EulerError = np.zeros(a)

b = Leibniz(a, LeibnizError)

c = Euler(a, EulerError)

print("According to Leibniz, Pi is roughly ", b)
print("\nAccording to Euler, Pi is actually ", c)

plt.plot(range(a), LeibnizError, range(a), EulerError)
plt.xlabel('Number of terms')
plt.ylabel('Error in approximating Pi')
plt.legend('LE')
plt.show()










