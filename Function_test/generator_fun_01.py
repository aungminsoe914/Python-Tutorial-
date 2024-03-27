def ge_test(val1,val2):
    for i in range(val1,val2+1):
        yield i
        
        
for i in ge_test(9,15):
    print("custom range is ",i)