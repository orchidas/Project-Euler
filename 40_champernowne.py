# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:25:53 2016

@author: ORCHISAMA
"""
#Problem - 40

#An irrational decimal fraction is created by concatenating the positive integers:
#
#0.123456789101112131415161718192021...
#
#It can be seen that the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

numlist = list()
cur = 1
while(True):
    s = str(cur)
    for char in s:
        if len(numlist) == 10**6:
            break
        numlist.append(char)
    if len(numlist) == 10**6:
        break
    cur += 1

prod = int(numlist[99]) * int(numlist[999])* int(numlist[9999]) * int(numlist[99999])
print prod