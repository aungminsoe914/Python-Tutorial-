input_one = int(input("Enter all subject number"))
isPass = True

for i in range(input_one):
    markone = float(input("entre mark of  "+str(i)+"   "))
    isPass = isPass and markone >=40
    
if isPass:
    print ("pass")
else:
    print("not pass")

