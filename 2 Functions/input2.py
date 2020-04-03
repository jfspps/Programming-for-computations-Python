# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 23:35:52 2020

@author: James Apps
"""

#def area(b, c):
#    return b*c
#
#x = input('Enter the base length: ')
#y = input('Enter the height: ')
#
#A = area(x, y)
#
##whitespace after 'is' is not required
#print 'The area of the rectangle is', A

print 'Computing the area of a triangle'

#try a triangle, make sure they coords are listed clockwise or anticlockwise
x = [1, 3, 2]
y = [1, 1, 4]

#arrays generally more efficient than lists
def areaPolygon(arrayX, arrayY):
    tempSum = 0
    for i in range(len(arrayX)-1):
        tempSum += arrayX[i]*arrayY[i+1]
    tempSum += arrayX[len(arrayX)-1]*arrayY[0]
    for i in range(len(arrayY)-1):
        tempSum -= arrayY[i]*arrayX[i+1]
    tempSum -= arrayY[len(arrayY)-1]*arrayX[0]
    return 0.5*tempSum

print 'Triangle area: ', areaPolygon(x, y)

#try a cube
x = [1, 3, 3, 1]
y = [1, 1, 4, 4]
print 'Cube area: ', areaPolygon(x, y)

#try a pentagon
x = [1, 3, 3, 2, 1]
y = [1, 1, 4, 5, 4]
print 'Pentagon area: ', areaPolygon(x, y)