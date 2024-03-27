def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 10)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 8)
        func(*args, **kwargs)
        print("%" * 5)
    return inner


@star
#@percent
def printer(msg):
    print(msg)

printer("Hello")