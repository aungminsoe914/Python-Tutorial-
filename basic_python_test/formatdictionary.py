p = {"id":1,"name":"ams"}

print("Name is :{x[name]} id :{x[id]}".format(x=p))

x = input("enter only char")

temp = ''

for n in x:
    if n.isalpha():
        temp = temp + n
        opt1=n
    else:
        temp = temp+chr(ord(opt1)+int(n))
print(temp)