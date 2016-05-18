# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:44:59 2016

@author: ORCHISAMA
"""
#Problem - 39

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
#there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p ≤ 1000, is the number of solutions maximised?
import math

def findSol(p):
    #smallest pythagorean pair = 3,4,5
    #assume a>b>c
    #max value of b for min value of a,i.e,3
    # b + 3 + root(b^2 + 3^2) = p
    b_uplim = ((p-3)**2 - 9)/(2*(p-3)) 
    count = 0
    for b in range(4,b_uplim):
        for a in range(3,b):
            c = math.sqrt(float(a**2) + float(b**2))
            if c.is_integer():
                if a+b+c == p:
                    print a,'+',b,'+',c,'=',p
                    count += 1
                elif a+b+c > p:
                    break
    return count
                
                
countarr = []
for n in range(14,1001):
    countarr.append(findSol(n))
    
print countarr.index(max(countarr)) + 14