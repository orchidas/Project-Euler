# #Project Euler Problem 85 - Count Rectangles

# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

# Solving by hand - 
# Let rectangle be axb sq units. Arrived at the equation
# ab (a+1)(b+1)/4 = two million
# Assume a to be 1 and solve for be to get:
# b^2 + b - 4,000,000 = 0
# b = (-1 + sq_root(1 + 4*4,000,000))/2

# Solving the quadratic equation yields 2000.5. But we need closest answer, hence we have to make some adjustments

import math
import sys


a = 1
b = 2000
desired_val = (2*10**6)
prev_error = sys.maxint

while a<=b:
	my_val = (a*b)*((a+1)*(b+1))/4
	cur_error = abs(desired_val - my_val)
	if cur_error < prev_error:
		area = a*b
		prev_error = cur_error
	if my_val > desired_val:
		b -= 1
	else:
		a += 1
	

print area

