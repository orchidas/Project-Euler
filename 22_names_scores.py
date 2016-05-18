# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:00:36 2016

@author: ORCHISAMA
"""
#Problem - 22
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is 
#the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
#What is the total of all the name scores in the file?

fh = open('names.txt','r')
text = fh.read()
names = text.split(',')
namelist = list()

print names

for name in names:
    #getting rid of quotes
    name = name[1:len(name)-1]
    namelist.append(name)
    
namelist.sort()
print namelist
nameprod = 0
for name in namelist:
    namevalue = 0
    if name.startswith('C'):
        print name
    for char in name:
        namevalue += ord(char) - 64
    namepos = namelist.index(name) + 1
    nameprod += namepos*namevalue
        
print nameprod