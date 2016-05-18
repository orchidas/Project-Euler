# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 01:10:51 2016

@author: ORCHISAMA
"""
#Problem - 69

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#
#n	Relatively Prime	φ(n)	n/φ(n)
#2	1	1	2
#3	1,2	2	1.5
#4	1,3	2	2
#5	1,2,3,4	4	1.25
#6	1,5	2	3
#7	1,2,3,4,5,6	6	1.1666...
#8	1,3,5,7	4	2
#9	1,2,4,5,7,8	6	1.5
#10	1,3,7,9	4	2.5
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

#n/phi(n) = 1/POS(1-1/p) where p is the set of prime numbers that are factors of the number n
#In this case we want to maximise n/phi(n). Therefore POS(1-1/p) should be as small as possible
#To do so, the number of prime factors need to be as high as possible

#We find the number below 1000000 that is yielded by multiplying the most number of primes
#For this we first generate upto the 500th prime number

import math

def genPrime():
    primelist = []
    primelist.append(2)
    primelist.append(3)
    
    for n in range(5,50000,2):
        flag = True
        if n%2 == 0 or math.sqrt(n).is_integer():
            continue
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i == 0:
                flag = False
                break
        if flag is True:
            primelist.append(n)
            
    print primelist       
    return primelist

    
primelist = genPrime()
limit = 10**6
num = 1
i = 0
while num < limit:
    num *= primelist[i]
    i += 1
    
num = num/primelist[i-1]
print num
        
        