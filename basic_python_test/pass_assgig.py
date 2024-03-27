z = [2,5,7]

x = 0
print (z)

x,z[x]= 2,20
print(x)
print(z[x])
print (z)


def fo():
    return (30,50)

r = fo()
x1,y1=r
print(x1)

o = 20
u =30
re = x1 if o<u else u
print("test re is ",re)
