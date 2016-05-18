# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 02:01:02 2016

@author: ORCHISAMA
"""
#Problem - 47

#The first two consecutive numbers to have two distinct prime factors are:
#
#14 = 2 × 7
#15 = 3 × 5
#
#The first three consecutive numbers to have three distinct prime factors are:
#
#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#
#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
import math

def primeFactors(n):
    factors = []
    while n%2 == 0:
        n = n/2
        factors.append(2)
        
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i == 0:
            factors.append(i)
            n = n/i
            
    #This condition is to handle the case when remaining n is a prime number
    #greater than 2       
    if n>2:
        factors.append(n)     
    #print factors
    return factors
    
    
nlist = []
for n in range(1000,10**6):
    primefactors = set(primeFactors(n))
    if len(primefactors) != 4:
        continue
    else:
        flag = True
        for i in range(n+1,n+4):
            if len(set(primeFactors(i))) != 4:
                flag = False
                break
        if flag is True:
            nlist.append(n)
            nlist.append(n+1)
            nlist.append(n+2)
            nlist.append(n+3)
            break
    
print nlist