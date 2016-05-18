# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:43:26 2016

@author: ORCHISAMA
"""
#Problem 64

#Notice that mn, dn, and an are always integers. The algorithm terminates when this triplet is the same as one encountered before. 
#The algorithm can also terminate on ai when ai = 2 a0 which is easier to implement.
import math

def recur(S):
    a = int(math.floor(math.sqrt(S)))
    a0 = a
    d = 1
    m = 0
    recurlist = []
    period = 0
    while a != 2*a0:
        period += 1
        recurlist.append(a)
        m = a*d - m
        d = (S-(m**2))/d
        a = int(math.floor((math.sqrt(S) + m)/d))
    #print recurlist, period
    return period

oddcount = 0
for n in range(2,10001):
    if math.sqrt(n).is_integer():
        continue
    else:
        period = recur(n)
        if period%2 == 1:
            oddcount += 1
            
print oddcount

    
    