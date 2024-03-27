def add(num1:int, num2:int)-> int:
	"""Add two numbers"""
	num3 = num1 + num2
    

	return num3

# Driver code
num1 = '5'
num2 =  10
ans = add(num1, num2)
print(type(ans))
#print(add("cla",30))
print(f"The addition of {num1} and {num2} results {ans}.")
print("The addition of {} and {} results {}.".format(num1,num2,ans))
