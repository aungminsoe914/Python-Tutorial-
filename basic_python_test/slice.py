g =['a','b','c','d']

print(g[slice(2)])


testslice = "helko string one"

x = slice(1,4,2)#
#slice(start,stop.step)
#can also slice string
print(testslice[x])
print(testslice[1:3])
print(testslice[:3])
print(testslice[1:])
print(testslice[:])
print(testslice[::-1])
print(testslice[:-1])