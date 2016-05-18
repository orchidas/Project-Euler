# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 02:31:41 2016

@author: ORCHISAMA
"""

# Problem 59

# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. 
# The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 
# 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge 
# that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.


#interesting problem on cryptography - do frequency analysis on given text
#tried all the things I learnt in Simon Singh's book!

def findkeybyAnalysis(freq):    
    output = list()
    for letter,value in freq.items():
        output.append((value,letter))
  
    #sort in descending order   
    output.sort(reverse = True)
    #print 'count value', output[0][0], 'letter', output[0][1]  
    # this value probably represents space bar whose ascii value is 32 (cheated on this)
    spacencr = output[0][1]
    key = 32 ^ int(spacencr)
    return key


def convertasciitostr(lst):
    mystr = ''
    for item in lst:
        mystr += chr(item)
    return mystr
    
    
fh = open('cipher.txt','r')
text = fh.read()
numbers = text.split(',')
freq1 = dict()
freq2 = dict()
freq3 = dict()
key = list()

#look at distributions of items 1,4,7,.....
for i in range(0,len(numbers),3):
    freq1[numbers[i]] = freq1.get(numbers[i],0) + 1
    if i < len(numbers) - 1:
        freq2[numbers[i+1]] = freq2.get(numbers[i+1],0) + 1
        freq3[numbers[i+2]] = freq3.get(numbers[i+2],0) + 1
      

#key is a 3 letter word
key = list()
key.append(findkeybyAnalysis(freq1))
key.append(findkeybyAnalysis(freq2))
key.append(findkeybyAnalysis(freq3))

print convertasciitostr(key)
encrypted = list()

for i in range(0,len(numbers),3):
    j = 0
    encrypted.append(int(numbers[i]) ^ key[j])
    if i < len(numbers)-1:
        encrypted.append(int(numbers[i+1]) ^ key[j+1])
        encrypted.append(int(numbers[i+2]) ^ key[j+2])
    
print 'The decrypted message is'
print convertasciitostr(encrypted)

sum = 0
for item in encrypted:
    sum += item
print sum
print len(numbers),len(encrypted)







