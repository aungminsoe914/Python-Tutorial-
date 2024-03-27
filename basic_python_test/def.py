def proc(*te):
    print("Process Tuple",te,type(te))
proc("a","b",1,2,"io")


loo = tuple(x for x in range(0,10))
print("first tuple is ",loo)
print("first tuple is ",tuple(loo))
