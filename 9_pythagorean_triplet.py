# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:18:32 2016

@author: ORCHISAMA
"""
#Problem - 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

a = 1
b = 31**2

while(True):
    c = math.sqrt(a**2 + b**2)
    if (a+b+c) == 1000:
        print a,b,c
        print a*b*c
        break
    elif (a+b+c) > 1000:
        b -= 1
        a = 1
    else:
        a += 1
            
            
           
        
    
    