#function to generate list of primes given upper limit

import math

def genPrime(upperlim):
    primelist = []
    primelist.append(2)
    primelist.append(3)
    
    for n in range(5,upperlim,2):
        flag = True
        if n%2 == 0 or math.sqrt(n).is_integer():
            continue
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i == 0:
                flag = False
                break
        if flag is True:
            primelist.append(n)
            
    #print primelist       
    return primelist