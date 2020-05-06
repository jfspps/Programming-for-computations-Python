# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:14:59 2020

@author: apps_
"""

#define functions first
def xy(x, y):
    """Here is where the docstring goes. This function
    computes the product of x and y"""
    return x*y;

#always list ordinary arguments before keyword argument
def multiplyByAConstant(i, con=10):
    """multiply i by a constant con"""
    return con*i;

#more compact lambda functions (which themselves can be passed as arguments)
addXAndY = lambda X, Y: X + Y 


z = xy(2.5, 2.5)
print(z)

print(multiplyByAConstant(3))

#overide the keyword argument (either pass in the same order or in any order with explicit labels)
print(multiplyByAConstant(3, con=20))
print(multiplyByAConstant(con=20, i=3))
print(multiplyByAConstant(3, 20))

print(addXAndY(1, 2))
X=1
Y=2
print(addXAndY(X, Y))