#Problem 65

e = []
e.append(2)

for i in range(2,151):
    if i%3 == 0:
        e.append(2*(i/3))
    else:
        e.append(1)
        
#print e
#by observation num[i] = num[i-2] + e[i]*num[i-1]
num = []
num.append(e[0])
num.append(e[0]+e[1])
for i in range (2,100):
    num.append(num[i-2] + e[i]*num[i-1])
    
sum = 0    
n = num[99]
while n>0:
    sum += n%10
    n = n/10
    
print num[99]
print sum