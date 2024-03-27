string_user =input("Enter a string eg,,This is a tree ")
#find keyward in a string
find_str = input ("wanted string")



def seart_str(find):
    if string_user.startswith(find) == True:
        print (f"Your keyword {find}is in start ")
    elif string_user.endswith(find) == True:
        print (f"Your keyword {find}is in end ")
    else:
        print (f"Your keyword {find}is not in this{string_user} ")
        
        
        
        
        
        
seart_str(find_str)