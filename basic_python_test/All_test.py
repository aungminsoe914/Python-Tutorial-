"""a =10
b =2
p =a+b
print("a is",a,b,p)
"""






#print("test")
test = ([1,2,3,4],"Another")
print(type(test))
print("Another tuple ",test)
test[0].append(100)
print("Another tuple",test)

#if else condition

num_01 = 40
temp_01 = "even" if num_01%2 == 0 else "odd"
print(temp_01)


#while not

while_01 ="one" 
while not while_01.isnumeric():
    print("one")
    break
    
    
    
    
#while not in

list_01= [0,1,2]
temp_02=0

while 8 not in list_01:
    if temp_02 not in  list_01:
        list_01.append(temp_02)
    else:
        temp_02+=1
print(list_01)