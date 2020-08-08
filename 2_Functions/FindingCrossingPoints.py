#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:37:43 2020

@author: james
"""


from numpy import linspace
import matplotlib.pyplot as plt

def f(x):
    return x

def g(x):
    return x**2

a = int(input('Enter the number of steps to plot: '))

b = float(input('Enter the difference epsilon required: '))

print("Finding points where f(x) and g(x) cross...")

x = linspace(-4, 4, a)

ymax = 0

for i in range(a):
    y = abs(f(x[i]) - g(x[i]))
    if y > ymax:
        ymax = y
    if y < b:
        print('Crossing found at x = ', x[i])

print('Maximum difference is ', ymax)