# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:09:57 2020

@author: apps_
"""


from sympy import *

x = Symbol('x')
y = Symbol('y')
print(2*x + 3*x - y)
print(diff(x**2, x))
print(integrate(cos(x), x))
print(limit(sin(x)/x, x, 0))
print(solve(5*x - 15, x))