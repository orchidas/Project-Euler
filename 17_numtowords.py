# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:27:03 2016

@author: ORCHISAMA
"""
#Problem - 17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
#The use of "and" when writing out numbers is in compliance with British usage.

numtowords = dict()
numtowords[0] = ''
numtowords[1] = 'one'
numtowords[2] = 'two'
numtowords[3] = 'three'
numtowords[4] = 'four'
numtowords[5] = 'five'
numtowords[6] = 'six'
numtowords[7] = 'seven'
numtowords[8] = 'eight'
numtowords[9] = 'nine'
numtowords[10] = 'ten'
numtowords[11] = 'eleven'
numtowords[12] = 'twelve'
numtowords[13] = 'thirteen'
numtowords[14] = 'fourteen'
numtowords[15] = 'fifteen'
numtowords[16] = 'sixteen'
numtowords[17] = 'seventeen'
numtowords[18] = 'eighteen'
numtowords[19] = 'nineteen'
numtowords[20] = 'twenty'
numtowords[30] = 'thirty'
numtowords[40] = 'forty'
numtowords[50] = 'fifty'
numtowords[60] = 'sixty'
numtowords[70] = 'seventy'
numtowords[80] = 'eighty'
numtowords[90] = 'ninety'


def extractDigits(n):
    diglist = list()
    while n>0:
        diglist.append(n%10)
        n = n/10
    units = ''
    tens = ''
    hundreds = ''
    thousands = ''  
    
    if diglist[0] != 0 :   
        units = numtowords[diglist[0]]
    if len(diglist) >= 2 :
        if diglist[1] == 1:
            tens = ''
            units = numtowords[diglist[1] * 10 + diglist[0]]
        else:    
            tens = numtowords[diglist[1] * 10]
        if len(diglist) >= 3 :
            hundreds = numtowords[diglist[2]] 
            if len(diglist) == 4:
                thousands = numtowords[diglist[3]]
        
    if hundreds != '':
        hundreds += 'hundred'
        if tens != '' or units != '':
            hundreds += 'and'
    if thousands != '':
        thousands += 'thousand'
        
    #words = thousands + " " + hundreds + " " + tens + " " + units
    #print words
    countwords = len(thousands) + len(hundreds) + len(tens) + len(units)
    return countwords
    
countsum = 0    
for i in range(1,1001):
    countsum += extractDigits(i)
    
print countsum
    
#print extractDigits(150)