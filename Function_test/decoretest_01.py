#Example 2: Passing the function as an argument 

def upper_a(text):
    print("Upper Case Returned",text.lower())
    return text.upper()
def lower_a(txt):
    print("Lower Case Returned",txt.lower())
    return txt.lower()


#two function calling in this function
def up_low_call(pass_fun):
    out_print=pass_fun("""This is a function / in two function call""")
    
    print(out_print)
    
    
    
up_low_call(upper_a)
up_low_call(lower_a)