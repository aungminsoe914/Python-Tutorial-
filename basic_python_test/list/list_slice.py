shopping_list = ['apples','pens','oatmeal ' ,'cookies','notepad','brushes','paint']

print(shopping_list[2:])
#['oatmeal ', 'cookies', 'notepad', 'brushes', 'paint']
print(shopping_list[:2])
#['apples', 'pens']
print(shopping_list[:])

#['apples', 'pens', 'oatmeal ', 'cookies', 'notepad', 'brushes', 'paint']

print(max(shopping_list))

print(shopping_list.pop(2))


test_loop = [122.01,132,120]
test_loop_ext = []
for i in test_loop:
    test_loop_ext.append(i)
    
    print(i)
print(test_loop_ext)