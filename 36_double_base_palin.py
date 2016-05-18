# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:44:16 2016

@author: ORCHISAMA
"""
#Problem - 36

#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
#(Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(s):
    l = len(s)
    for i in range(0,l/2):
        if s[i] != s[l-1-i]:
            return False
    return True
    
def toBinary(n):
    bin = list()
    while n > 0:
        bin.append(n%2)
        n = n/2
    bin.reverse()
    return bin
    
sumlist = 0
for n in range(1,10**6):
    binlist = toBinary(n)
    if isPalindrome(str(n)) and isPalindrome(binlist):
        print n, str(binlist)
        sumlist += n
        
print 'The sum is', sumlist
    
