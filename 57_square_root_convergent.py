# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 01:40:00 2016

@author: ORCHISAMA
"""
#Problem - 57

#It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
#√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
#By expanding this for the first four iterations, we get:
#
#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
#The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example 
#where the number of digits in the numerator exceeds the number of digits in the denominator.
#
#In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

def countdig(num):
    dig = 0
    while num>0:
        dig += 1
        num = num/10
    return dig
        

#def rec(num, den, count, lcount):
#    if count == 1000:
#        return lcount
#    else:
#        #expansion += 1 + 1/(1 + expansion)
#        numCopy = num
#        num = 2*den + num
#        den = den + numCopy
#        #print num, '/', den
#        if countdig(num) > countdig(den):
#            lcount += 1
#        count += 1
#        return rec(num, den, count, lcount)
        
        
        
num = list()
den = list()
lcount = 0
num.append(1)
den.append(1)
for i in range(1,1000):
    num.append(2*den[i-1] + num[i-1])
    den.append(num[i-1] + den[i-1])
    if countdig(num[i]) > countdig(den[i]):
        lcount += 1
    
print lcount    
    
    
   