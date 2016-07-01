#Project Euler Problem 92

def digitSquare(num):
	sum_sq = 0
	for digit in str(num):
		dig = int(digit)
		sum_sq += dig**2
	return sum_sq


upperlim = 10**7
count = 0
for i in range(2,upperlim):
	sum_sq = digitSquare(i)
	while(sum_sq != 89 or sum_sq != 1):
		if sum_sq == 89 :
			count += 1
			break
		if sum_sq == 1:
			break
		sum_sq = digitSquare(sum_sq)


print count
