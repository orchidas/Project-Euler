# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 01:29:03 2016

@author: ORCHISAMA
"""

# Problem - 50
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


import math

def genPrime():
    primelist = []
    primelist.append(2)
    primelist.append(3)
    
    for n in range(5,10**6,2):
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
    

primelist = genPrime()
consecutive = ()

for j in range(0, len(primelist)):
    i = j
    sum = 0
    while sum < 10**6 and i < len(primelist):
        sum += primelist[i]
        i += 1
        
    sum -= primelist[i-1]
    if sum in primelist:
        print i-j-1, sum
        consecutive = (i-j-1,sum)
        break

print consecutive       
        
    
    