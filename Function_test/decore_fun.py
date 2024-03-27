def make_pretty(funce):

    def inner():
        print("I got decorated")
        funce()
    return inner

@make_pretty
# @make_pretty must be same def make_pretty(func)'s name
def ordinary():
    print("I am ordinary")
#@make_pretty
def secondary():
    print("I am secondary")

secondary()
ordinary()  

