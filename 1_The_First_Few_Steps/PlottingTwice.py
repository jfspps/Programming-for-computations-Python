# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:33:32 2020

@author: apps_
"""


from numpy import zeros
import matplotlib.pyplot as plt

#setup the average heights for each family member
h = zeros(4)
h[0] = 1.60; h[1] = 1.85; h[2] = 1.75; h[3] = 1.80
H = zeros(4)
H[0] = 0.50; H[1] = 0.70; H[2] = 1.90; H[3] = 1.75

family_member_no = zeros(4)
family_member_no[0] = 0; family_member_no[1] = 1
family_member_no[2] = 2; family_member_no[3] = 3

#this plots two curves, x vs y (as opposed to y against x)
plt.plot(family_member_no, h, family_member_no, H)
plt.xlabel('Family member number')
plt.ylabel('Height (m)')
plt.legend('hH')
plt.show()