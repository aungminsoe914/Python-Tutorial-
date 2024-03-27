#from calculator import add,mul
#from calculator import *
#import calculator as c
#import calculator
import importlib
import calculator
importlib.reload(calculator)
from calculator import add as a
#import dis
print(a(2,3))
##print(calculator.mul(3,4))

#print ("dis is ",dis.dis(calculator.add))