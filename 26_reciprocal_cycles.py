# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:51:55 2016

@author: ORCHISAMA
"""
#Problem - 26
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part


checklim = 1000

def findFracDigits(n):
    digits = list()
    numdig = len(str(n))
    numerator = 10**numdig
    for i in range(numdig-1):
        digits.append(0)
    
    while len(digits) < checklim:
        digits.append(numerator/n)
        numerator = (numerator % n) * 10**numdig
        if numerator == 0:
            return digits
            
    return digits
        
        
def findRecurringCycle(n):
    postdecimal = findFracDigits(n)
    pos = list()
    for digits in postdecimal:
        pos.append(postdecimal.index(digits))
     
    if len(pos) < checklim:
        return 0
    
    for i in range(len(pos)-1):
        if pos[i+1] < pos[i]:
            return pos[i]
    return 1
        

recurlist = list()    
for i in range(11,1000):
    recurlist.append(findRecurringCycle(i))

print max(recurlist)    
print recurlist.index(max(recurlist)) + 11
    
    
    
