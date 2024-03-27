# the function call itself repeatly
#call recursive function

def rec_fun(n):
    if n == 0:
        r = 1
    else:
        r = n*rec_fun(n-1)
    return r
print("Factional : ",rec_fun(6))    
print("Factional : ",rec_fun(7))    

