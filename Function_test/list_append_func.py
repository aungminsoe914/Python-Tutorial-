def lifun(list_one=[]):
    list_one.append(100)
    return list_one
list_two=[1,2,3,4,5]
result_one = lifun(list_two)
print("Append in function of list is - ",result_one)