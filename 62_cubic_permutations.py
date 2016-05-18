# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:48:51 2016

@author: ORCHISAMA
"""

#The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
#In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

#for five permutations of a number, it has to be 3 digit, or more (3P3 = 6). The first 3 digit cube is 125
#5^3. Therefore we start from n = 5

##hey I wrote a smart solution
def genCube(n):
    return (n,''.join(sorted(str(n**3))))
#sort all the digits in the number and join to form a string.
#All cubes having same digits will have same sorted string of digits
    

cubelist = []
for n in range(5,10000):
    cubelist.append(genCube(n))
    
cubecount = dict()
cubedict = dict()
cubelist.sort()

for n,cube in cubelist:
    cubedict[cube] = cubedict.get(cube,[]) +[n]


for n,cube in cubelist:
    cubecount[cube] = cubecount.get(cube,0) + 1
    if cubecount[cube] == 5:
        print cubedict[cube]
        print min(cubedict[cube])**3
        break
    

       
        
    
