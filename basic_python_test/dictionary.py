student = {"ro1":"aungminsoe","rol2":"mg mg soe"}
print(student)
print(type(student))
print("Roll 1 student name is ",student.get("ro1"))
student["rol2"] = "soe maung"
print(student)


for key,val in student.items():
    print("roll number is ",key,"and name is " , val)
    print("This is ",student.items())