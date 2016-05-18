# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 23:02:21 2016

@author: ORCHISAMA
"""

#Problem 66 - diophantine equation x^2 - Dy^2 = 1
#For given D, minimise x

#Consider quadratic Diophantine equations of the form:
#
#x2 – Dy2 = 1
#
#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
#It can be assumed that there are no solutions in positive integers when D is square.
#
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
#32 – 2×22 = 1
#22 – 3×12 = 1
#92 – 5×42 = 1
#52 – 6×22 = 1
#82 – 7×32 = 1
#
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


#one solution is to get the convergent of sqrt(D) = n_i/d_i
#till - D*d_i = 1
#see odd_period_square_roots to know how to generate continued fractions of square roots
#see e_convergent to generate convergants of a square root

import math
diophantine = []

for D in range(2,1001):
    if math.sqrt(D).is_integer():
        continue
    
    limit = int(math.floor(math.sqrt(D)))
    a = limit
    m = 0
    d = 1
    
    num1 = 1
    num = a
    den1 = 0
    den = 1
    
    while num**2 - D*(den**2) != 1:
        m = a*d - m
        d = (D-(m**2))/d
        a = (limit + m)/d
        
        num2 = num1
        num1 = num
        den2 = den1
        den1 = den
        
        num = num1*a + num2
        den = den1*a + den2
        
    diophantine.append((num,D))
    

diophantine.sort(reverse = True)
print diophantine[0]

    
        
        
        
        
        