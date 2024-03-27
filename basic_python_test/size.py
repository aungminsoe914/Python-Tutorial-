import sys

x = 10
print("size of x is ", sys.getsizeof(x),"bytes")
print("refrence count of x is ", sys.getrefcount(x),"bytes")