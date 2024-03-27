print((lambda x: x + 1)(2))

xc = lambda xu : xu + 1

print(xc(8))



print((lambda x, y, z: x + y + z)(1, 2, 3))



print( (lambda x, y, z=3: x + y + z)(1, 2))

print( (lambda x, y, z=3: x + y + z)(1, y=2))

print( "sum of 1,2,3 is ",(lambda *args: sum(args))(1,2,3))

print( "***lambda ***argv is /",(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

print( (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))


number = 'one','two','three'
funcs =[]
print(type(number))
for n in number:
    funcs.append(lambda n=n:print(n))
for f in funcs:
    f()
    

print("////////////////////////////////")
number = 'one','two','three'
funcs =[]
print(type(number))
for n in number:
    funcs.append(lambda:print(n))
for f in funcs:
    f()
    

