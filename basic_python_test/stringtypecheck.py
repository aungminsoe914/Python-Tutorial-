stringte = input("Enter String")

if stringte.isalnum():
    print("Alpha numeric")
    if stringte.islower():
        print("Alpha is lower")
    else:
        print("not lower")
else:
    print("not alphanumeric")