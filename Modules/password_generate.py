from random import*
import string


pwe =''
pwd_length_01 = 7
for i in range(pwd_length_01):
    if random()>0.4:
       pwe += choice(string.ascii_letters)
    else:
         pwe += choice(string.digits)

print(pwe)        