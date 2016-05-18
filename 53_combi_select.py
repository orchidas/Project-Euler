# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:51:53 2016

@author: ORCHISAMA
"""
#Problem - 53

#There are exactly ten ways of selecting three from five, 12345:
#
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#In combinatorics, we use the notation, 5C3 = 10.
#
#In general,
#
#nCr =	
#n!
#r!(n−r)!
#,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
#How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    return fact

combicount = 0
for n in range(23,101):
    num = factorial(n)
    for r in range(2,n/2+1):
        combi = num/(factorial(r) * factorial(n-r))
        if combi > 10**6:
            print n, r
            if n%2 == 0:
                combicount += 2*(n/2-r+1) - 1
            else:
                combicount += 2*(n/2-r+1)
            break
    
print combicount
        
    