def cla():
    yield 1
    yield 2
    yield 3
    yield 4
    
call_generator = cla()

print(call_generator)
print(type(call_generator))

#normal calling
print(next(call_generator))
print(next(call_generator))
print(next(call_generator))
print(next(call_generator))

#loop calling
for i in cla():
    if i == 1:
        print("I is one ")
    else:
        print("I is ",i)
    
