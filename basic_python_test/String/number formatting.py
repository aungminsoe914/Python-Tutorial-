#print(f"This is a string{aungminsoe:x}")
print("The mangy, scrawny stray dog %s gobbled down" %'hurriedly' 
      +"the grain-free, organic dog food.")
x = 'looked'
print("hello ",x)
print("Misha %s and %s around"%('walked',x))
#:4f
print('The value of pi is: %5.4f' %(3.141592))
#In the given code, the formatting string
# Python is converted to Integer and floating point with %d,%f.
variable = 12
string = "Variable as integer = %d \n\
Variable as float = %f" %(variable, variable)
print (string)
#Real
#Real used my 
#print('{2} {1} {0}'.format('directions','the', 'Read'))
print('{2} {1} {0}'.format('directions','the', 'Read'))

#Insert object by Assigning Keywords
print('a: {a}, b: {b}, c: {c}'.format(a = 1,
									b = 'Two',
									c = 12.3))

#Reuse the inserted objects
print(
	'The first {p} was alright, but the {p} {p} was tough.'.format(p='second'))


#################
print('The valueof pi is: %1.5f' %3.141592)
print('The valueof pi is: {0:1.5f}'.format(3.141592))




