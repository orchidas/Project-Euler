# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 00:05:45 2016

@author: ORCHISAMA
"""
#Problem - 38
#Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. 
#We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
#giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated 
#product of an integer with (1,2, ... , n) where n > 1?

#Solution:
#largest possible 9 digit number = 999999999
#concatenated product of 1 and (1,2,3...9) = 123456789
#let's start testing with 4 digit numbers, with MSD = 9. No repitions of digits allowed 

def findPandigital(num):
    prod = 0
    i = 1
    str1 = ''
    while(prod <= 999999999):
        toadd = num * i
        if int(str1 + str(toadd)) > 999999999:
            #check if all digits in the number are unique
            charlist = sorted(str1)
            j = 1
            for char in charlist:
                if char != str(j):
                    return -1
                j = j+1    
            return prod
            
        str1 = str1 + str(toadd)
        prod = int(str1)
        i = i + 1
    
lst = list()
for num in range(9000,10000):
    print 'Pandigital multiples of',num,'is being calculated'
    lst.append(findPandigital(num))
    
max = 0
for item in lst:
    if item > max:
        max = item
        
print max        
    
    
