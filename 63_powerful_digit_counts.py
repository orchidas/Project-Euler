# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 02:54:29 2016

@author: ORCHISAMA
"""
#Problem - 63
#The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
#How many n-digit positive integers exist which are also an nth power?

#n digit number = x^n
#10^n has n+1 digits
#range of x = 1 to 9

nsum = 0
for n in range(1, 100):
    for x in range(1,10):
        if len(str(x**n)) == n:
            print n,x**n
            nsum += 1
            
print nsum