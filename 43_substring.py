# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:49:42 2016

@author: ORCHISAMA
"""
#Problem - 43

#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17

#Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools

def checkSubstring(n):
    strnum = str(n)
    primelist = [2,3,5,7,11,13,17]
    for i in range(len(primelist)):
        substr = int(strnum[i+1:i+4])
        if(substr % primelist[i] == 0):
            continue
        else:
            return 0
    return n        
        
        
#print checkSubstring(1406357289)

#generate all 9 digit pandigital numbers
diglist = '0123456789'
allPandigit = list()

permutations = set(itertools.permutations(diglist))
for item in permutations:
    permstr = ''
    if item[0] == '0': continue
    for character in item:
        permstr += character
    allPandigit.append(int(permstr))

   
sum = 0    
for pandigit in allPandigit:
    sum += checkSubstring(pandigit)
    
print sum    
    

    