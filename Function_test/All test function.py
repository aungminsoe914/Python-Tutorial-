#parameter string and number pass in function
def nameAge(name: int, age: int)-> int:
    #print(type(name))
    
	print("Hi, I am", name)
	print("My age is ", age)
    


# You will get correct output because 
# argument is given in order
print("Case-1:")
x="Suraj"
nameAge(x, 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")



#/////////////////////////////////

def our_sum(*number):
    print("Numbers ",number)
    return sum(number)
print("Sum ",our_sum(1,2))


