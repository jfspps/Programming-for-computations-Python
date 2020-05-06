# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:10:22 2020

@author: apps_
"""


from numpy import linspace
import matplotlib.pyplot as plt
import random

x1 = random.randrange(-10,-6, 1)
x2 = random.randrange(5, 10, 1)
diff = x2 - x1
print(str(x1) + " " + str(x2))
x=linspace(x1,x2,diff)
y=x**5 + x + 5

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('x**5 + x + 5')