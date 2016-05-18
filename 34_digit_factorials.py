# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:50:27 2016

@author: ORCHISAMA
"""
#Problem - 34
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
        
factorial = list()        
for n in range(10):
    factorial.append(fact(n))
        
def findDigits(n):
    digits = list()
    while n>0:
        digits.append(n%10)
        n = n/10
    return digits
    
def findDigitSumFact(n):
    digits = findDigits(n)
    sumfact = 0
    for item in digits:
        if sumfact > n:
            return False
        sumfact += factorial[item]
    if sumfact == n:
        return True
    return False

   
lowerlim = 44
upperlim = 10**6 #guessing!
sum = 0

for n in range(lowerlim, upperlim):
    if findDigitSumFact(n) is True:
        print n
        sum += n

print sum
    
    



    

    
    