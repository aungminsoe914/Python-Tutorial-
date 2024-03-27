from random import *
import string


print("String is ",string.ascii_uppercase)
print(choice(string.ascii_uppercase))
print("String digits is ?",choice(string.digits))
pwe = ""
pwd_length = 15
for i in range(pwd_length):
    pwe += choice(string.ascii_letters)
print("password choice is ",pwe)
    
