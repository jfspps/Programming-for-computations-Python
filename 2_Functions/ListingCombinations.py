#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:31:32 2020

@author: james
"""


# Listing the combinations, using m1*m2*m3*m4 where m1 etc represents the number
# of configurations of the first item, m2 represents the second item, and so on

print("A deck of cards has 13 ranks: A, 2-10, J, Q and K. There are four" + 
      " suits: C, D, S and H. A total of 52 combinations")

suits = ['C', 'D', 'S', 'H']

ranks = ['A', '2', '3', '4', '5', '6', '7',
         '8', '9', '10', 'J', 'Q', 'K']

deck = []

for s in suits:
    for r in ranks:
        deck.append(s + r)
print(deck)

print("The roll of a die yields 1 to 6 eyes. With two rolls, we should see 36 "+
      "combinations")

eyes = ['1', '2', '3', '4', '5', '6']

rolls = []

count = 0   # number of sums of eyes which equal 7

for i in eyes:
    for j in eyes:
        rolls.append(i + j)
        if (int(i) + int(j) == 7):
            count += 1

print(rolls)

print("Number of sums of seven is", count)