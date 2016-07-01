#Project Euler - Problem 37 - Truncable Primes

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits 
#from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math
from prime import genPrime

primelist = list()
primelist = genPrime(10**6)
sumlist = 0
count = 0

#single digit primes cannot be truncable
for prime in primelist[8:]:
	r2l = prime
	l2r = prime
	flag = True
	r2l /= 10
	l2r %= 10**(len(str(l2r))-1) 

	while r2l > 0:
		try:
			indx = primelist.index(r2l)
			indy = primelist.index(l2r)
		except:
			flag = False
			break
		r2l /= 10
		l2r %= 10**(len(str(l2r))-1)

	if flag is True:
		sumlist += prime
		count += 1
		print prime, count

	if count == 11:
		break

print 'The sum of truncable primes is:'	
print sumlist, count


