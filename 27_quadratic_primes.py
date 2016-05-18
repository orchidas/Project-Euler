# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 22:48:19 2016

@author: ORCHISAMA
"""

# Problem - 27

# Euler discovered the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 
# is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

#     n² + an + b, where |a| < 1000 and |b| < 1000

#     where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |−4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n,
#  starting with n = 0.

import math

def genPrime(upperlim):
    primelist = []
    primelist.append(2)
    primelist.append(3)
    
    for n in range(5,upperlim,2):
        flag = True
        if n%2 == 0 or math.sqrt(n).is_integer():
            continue
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i == 0:
                flag = False
                break
        if flag is True:
            primelist.append(n)
            
    #print primelist       
    return primelist


def isPrime(n, primelist):
    i = 0
    while n >= primelist[i]:
        if n == primelist[i]:
            return True
        i += 1
    return False
    
    
prime = genPrime(1000)
maxPrime = 0
maxN = 0
primelist = genPrime(10**6)
for a in range (-999,1001):
    for b in prime:
        if b == 2  and a%2 == 1:
            continue
        elif b > 2 and a%2 == 0:
            continue
        else:
            for j in range(0,2):
                sign = 1 if j==0 else -1
                n = 0
                while n < abs(a) and isPrime(n**2 + a*n + sign*b, primelist):
                    n += 1
                if n>maxN:
                    maxN = n
                    maxPrime = a*sign*b
                        
print maxN, maxPrime