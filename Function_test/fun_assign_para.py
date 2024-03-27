def sum(a,b):
    print("a,b sum is ",a+b)
    
x = sum
def call_x():
    return x(8,1)

call_x()


lam_test = (lambda x : call_xc())
call_xc = (lambda x : x+1)(2)
#(lambda x: x + 1)(2)

print(lam_test)