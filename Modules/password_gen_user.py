#this program will show user generete password len showed

from random import *
import string




"""def generate_pass(len_pass):
    for i in range(len_pass):
        pwd = ''
        if random()>0.9:
            pwd += choice(string.ascii_uppercase)
        else:
            pwd += choice(string.digits)
    print(pwd)
    
    
use_pass =input("Enter number for generate password")
generate_pass(use_pass)
"""
"""def gene_two():
    pwe =''
    pwd_length_01 = 7
    for i in range(pwd_length_01):
        if random()>0.4:
        pwe += choice(string.ascii_letters)
        else:
            pwe += choice(string.digits)

    print(pwe)        
    
   """ 
    
def gene_pass(lenpa):
    pwd = ""
    pwd_leng = lenpa
    for i in range(pwd_leng):
        if random() >0.4:
            pwd += choice(string.ascii_uppercase)
        else:
            pwd += choice(string.digits)
    print(pwd)
    
    
user_item =int( input("Enter Digit"))
gene_pass(user_item)

