# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 01:27:38 2016

@author: ORCHISAMA
"""
#Problem - 46

#It was proposed by Christian Goldbach that every odd composite number can be written as the 
#sum of a prime and twice a square.

#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2
#
#It turns out that the conjecture was false.
#
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def findPossibleSquares(num):
    sqr = list()
    for n in range(1,num):
        if 2*(n**2) < num:
            sqr.append(2*(n**2))
        else:
            break
    return sqr    
 
    
def isPrime(n):
    for i in range(2,n/2 + 1):
        if n % i == 0:
            return False
    return True        

           
def check(num, sqr):   
    for squares in sqr:
        primeNum = num - squares
        res = isPrime(primeNum)
        if primeNum > 0 and res is True:
            return True
        else: continue
    
    return False
          
        
num = 3
sqr = list()
while(True):
    flag = isPrime(num)
    if flag is True:
        num = num + 2
        continue
    else:
        sqr = findPossibleSquares(num)
        res = check(num, sqr)
        if res is True:
            num = num + 2
        else:
            print num
            break
            

    
    
    
    