# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:11:27 2016

@author: ORCHISAMA
"""
#Problem - 33

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

#to reduce fractions to their lowest value, divide numerator and denominator by the HCF
def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b,a%b)

def checkCondition(num1,num2,den1,den2):
    if num1 == den1 and num2 != den2:
        return (True, num2, den2)
    elif num1 == den2 and num2 != den1:
        return (True, num2, den1)
    elif num2 == den1 and num1 != den2:
        return (True, num1, den2)
    elif num2 == den2 and num1 != den1:
        return (True, num1, den1)
    else:
        return (False, )
    
    
def checkFraction(num, den):        
    numdig1 = num%10
    numdig2 = num/10
    dendig1 = den%10
    dendig2 = den/10
    res = checkCondition(numdig1, numdig2, dendig1, dendig2)
    if res[0] is True:
        numdig = res[1]
        dendig = res[2]
        gcd = hcf(den,num)
        den /= gcd
        num /= gcd
        gcd = hcf(dendig,numdig)
        dendig /= gcd
        numdig /= gcd
        if dendig == den and numdig == num:
            return True
        else:
            return False
    else:
        return False
    
        
strlist = []
for den in range(11,100):
    for num in range(10, den):
        if num%10 == 0 and den%10 == 0:
            continue
        else:
            if checkFraction(num, den) is True:
                strlist.append(str(num)+'/'+str(den))

print strlist
    