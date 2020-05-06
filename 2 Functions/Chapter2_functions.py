# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:23:47 2020

@author: James Apps
"""

def y(v0y, t):
    g = 9.81
    return v0y*t - 0.5*g*t**2
    
def x(v0x, t):
    return v0x*t
    
def two_funcs(v0x, v0y, t):
    return x(v0x, t), y(v0y, t) 
    
#always place keyword (named) parameters after ordinary (positional) arguments
def two_funcsDefault(v0x, v0y, t=0.5):
    """this has a default value t=0.5"""
    return x(v0x, t), y(v0y, t) 

#example of a lambda function
f = lambda x, y: x + 2*y

initial_velocity_x = 2.0
initial_velocity_y = 5.0

time = 0.6
print x(initial_velocity_x, time), y(initial_velocity_y, time)
#achieves the same thing...
print "returning a tuple"
print two_funcs(initial_velocity_x, initial_velocity_y, time)

print two_funcs(initial_velocity_x, initial_velocity_y, 0.9)

print two_funcsDefault(initial_velocity_x, initial_velocity_y)
#override the default value
print two_funcsDefault(initial_velocity_x, initial_velocity_y, t=0.9)

print "Lambda function: "
print f(2, 5)