# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:26:29 2016

@author: ORCHISAMA
"""
#Problem - 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.


def findDivisorSum(n):
    divisor = 0
    for i in range(1,n/2+1):
        if n % i == 0:
            divisor += i
    return divisor

    
amicableSum = 0
alreadychecked = list()
for num in range(1,10000):
    sum1 = findDivisorSum(num)
    # if the pair has already been checked, skip the rest of the steps
    if num in alreadychecked and sum1 in alreadychecked:
        continue
    else:
        alreadychecked.append(num)
        alreadychecked.append(sum1)   
        sum2 = findDivisorSum(sum1)
        if sum2 == num and sum1 != num:
            print num,sum1
            amicableSum += num + sum1
        
print amicableSum
        
