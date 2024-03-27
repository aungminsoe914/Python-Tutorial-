def fun_one(paa_arg):
    print("Print argument one")
    paa_arg()
    
    
def fun_two():
    print("Print function two")
    
def func_three():
    print("Print function three")
    
assign = fun_one(func_three)
print(assign)




#Refrance From
#https://www.geeksforgeeks.org/decorators-in-python/
