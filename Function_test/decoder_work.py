def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
# @make_pretty must be same def make_pretty(func)'s name
def ordinary():
    print("I am ordinary")

ordinary()  