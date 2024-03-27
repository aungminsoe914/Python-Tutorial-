l = [20,30,40]

f = False
ind = 0
get_user = int(input("Enter number want to find"))

while not f:
    if(l[ind] == get_user ):
        print("value found at index ",ind)
        break
    else:
        ind+=1
        
        
#while not in

list_01= [0,1,2]
temp_02=0

while 8 not in list_01:
    if temp_02 not in  list_01:
        list_01.append(temp_02)
    else:
        temp_02+=1
print(list_01)
    
    