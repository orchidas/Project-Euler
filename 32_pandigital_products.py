# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:12:24 2016

@author: ORCHISAMA
"""

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

#100 * 100 = 10000 - 11 digits
#100 * 10 = 10000
#999 * 99 = 98901
#x * y = 9 digit product - what are the possible values of x and y
# range of x = 100 to 999  #repition of digits and 0 not allowed, range changes to 123 to 987
# range of y = 10 to 99
#4987 * 2 = 9974
#3 digit * 2 digit = 4 digit
#4 digit * 1 digit = 4 digit

#Problem - 32

def checkRepeatDigits(n):
    dig = dict()
    for i in range(10):
        dig[i] = 0
        
    while n>0:
        dig[n%10] += 1
        n = n/10
        
    for i in range(10):
        if dig[i] > 1:
            return True
    return False

    
def checkPandigital(string):
    string = sorted(string)
    for i in range(1,10):
        if string[i-1] != str(i):
            return False
    return True

def exists(elem, lst):
    for item in lst:
        if item == elem:
            return True
    return False
    

prodsum = 0
prodlist = list()
# 3 digit * 2 digit = 4 digit
for i in range(123,987):
    if checkRepeatDigits(i) is True:
        continue
    for j in range(12,98):
        prod = i*j
        if prod >= 10000:
            break
        if checkRepeatDigits(j) is True:
            continue 
        if checkPandigital(str(i) + str(j) + str(prod)):
            if not exists(prod, prodlist):
                prodlist.append(prod)
                print i,j,prod
            
# 4 digit * 1 digit = 4 digit
for i in range(1234, 4987):
    if checkRepeatDigits(i) is True:
        continue
    for j in range(2,9):
        prod = i*j
        if prod >= 10000:
            break
        if checkRepeatDigits(j) is True:
            continue
        if checkPandigital(str(i) + str(j) + str(prod)): 
            if not exists(prod, prodlist):
                prodlist.append(prod)
                print i,j,prod
                    
for prod in prodlist:
    prodsum += prod
    
print prodsum
    