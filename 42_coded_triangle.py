# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 00:49:51 2016

@author: ORCHISAMA
"""
#Problem - 42

#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position 
#and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand 
#common English words, how many are triangle words?


import math

def checkTriangle(num):
    a = 1
    b = 1
    c = -(num*2)
    sqr = b**2 - 4*a*c
    if sqr < 0:
        return False
    else:
        root1 = (-b + math.sqrt(sqr))/(2*a)
        if root1.is_integer() is True:
            return True
        else:
            return False
        

fh = open('words.txt')
text = fh.read()
words = text.split(',')
count = 0
res = False 
for word in words:
    word = word[1:len(word)-1] #removing semicolons
    print word
    num = 0
    for letter in word:
        num = num + ord(letter) - 64
    res = checkTriangle(num)
    if res is True:
        count = count + 1
    
print count    

#print checkTriangle(55)