s_wide = {x+x for x in range(10)}
print(s_wide)
print(type(s_wide))
print(list(s_wide)[2])


#Remove fandamental element from list
#list
list_one = [1,2,3,1]
print("list is ",list_one)
#remove one
#change set type
set_one = set(list_one)
print("Remove one from list change set after ",set_one)
#change list
list_one_change = list(set_one)
print("list change set change after list ,Result is ",list_one_change)



phone_numbers = { 'Jack': '070-02222748',
                      'Pete': '2488634' ,
                      'myanmar':'123'}
phone_numbers['Jack'] = '1234567'
print(phone_numbers)
print(phone_numbers.keys())
print(phone_numbers.items())
print(phone_numbers.values())
set_de = 'myanmar'
print("key is ",phone_numbers.setdefault(set_de))
