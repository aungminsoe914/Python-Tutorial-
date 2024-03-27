netlist = [[1,2,3],[4,5,6]]
print(netlist)
for i in netlist:
    for item in i:
        print("Nested list item is ",item)
        
print(enumerate(netlist))
for row,rowitm in enumerate(netlist):
    print("Row is ",row,"Row Item is ",rowitm)
    for col,colitm in enumerate(rowitm):
        print("col is ",col , "Column item is ",colitm)
        
    
    
    
netlistone =[1,3,4,5,6,]
print(netlistone)
lion=[]
for littwo in netlistone:
    #li = littwo*2
    lion.append(littwo*2)
    #print(li)
    print(lion)
    
    
cc =["apple","Orange","bannnNa"]
listtwo = [(x.upper(),len(x)) for x in cc]
print(listtwo)



