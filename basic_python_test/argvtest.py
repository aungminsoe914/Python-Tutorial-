marks = [("myanmar",30),("english",40),("bio",90)]
print(type(marks))

passsub = [subject for subject in marks if subject[1]>=90]
print("Pass subject is ",passsub)
