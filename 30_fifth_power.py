# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:47:56 2016

@author: ORCHISAMA
"""
#Problem 30

#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#1634 = 1^4 + 6^4 + 3^4 + 4^4
#8208 = 8^4 + 2^4 + 0^4 + 8^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 1^4 is not a sum it is not included.
#
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#brute force method 

p = 5
def findDigits(n):
    digit = list()
    while n>0:
        digit.append(n%10)
        n = n/10
    return digit


def findsumfifthpower(n):
    digits = findDigits(n)
    sumpow = 0
    for item in digits:
        sumpow += item**p
        if sumpow > n:
            return 0
        
    if sumpow == n:
        return sumpow
    else:
        return 0
        

lowerlimit = 3**(p) # 3^5 (1^5 and 2^5 are too small)
upperlimit = 9**(p+1)  #(max number = 9^5+9^5+...9times)
sum = 0
for i in range(lowerlimit, upperlimit+1):
    sum += findsumfifthpower(i)
    
print sum

