# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:23:53 2016

@author: ORCHISAMA
"""
#
#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#
#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

import math
def checkPent(n):
    a = 3
    b = -1
    c = -2*n
    D = float(b**2 - 4*a*c)
    if(D < 0):
        return False
    else:
        root = (-b + math.sqrt(D))/(2*float(a))
        if root.is_integer():
            return True
        else:
            return False
        

def generatePen(num):
    pent = []
    for n in range(1,num):
        pent.append(n*(3*n-1)/2);
    return pent
    
num = 5000  
pent = generatePen(num)
leastdiff = []
#print pent

for i in range(2,num-1):
    for j in range(i-1,0,-1):
        if checkPent(pent[i]-pent[j]) and checkPent(pent[i]+pent[j]):
            print pent[i] + pent[j], pent[i] - pent[j]
            leastdiff.append(pent[i] - pent[j])
            break
    
   
print min(leastdiff)
    
