def testnon():
    i=1
    print("first value is ",i)
    def testnon_one():
        nonlocal i
        i = i +1
        print("second value is",i)
        return i
    return testnon_one
next_two=testnon()
#print(testnon())
print(next_two())
next_two()