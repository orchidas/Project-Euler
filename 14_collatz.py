# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:46:18 2016

@author: ORCHISAMA
"""
#Problem - 14
#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?

upperBound = 10**6

# check for n = 999999. Largest possible odd number below 1 million
num = 999999

def checkSequence(n, count):
    if n == 1:
        return count
    else:
        if n%2 == 0:
            return checkSequence(n/2, count+1)
        else:
            return checkSequence(3*n + 1, count+1)
            

#print checkSequence(13,1)            
countlist = list()
for i in range(1,10**6):
    countlist.append(checkSequence(i,1))
    
print countlist.index(max(countlist))+1
        
