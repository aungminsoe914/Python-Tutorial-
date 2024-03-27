import dis

a = 10
b = 20
c = 30

def func():
    d = a + b * c
    return d
#print (func())

#dis.dis(func)
print(dis.dis(func()))