'''
Typically, during variables, you want them to make sense to you and to the reader. 

You can also provide a default value into the function

Typically, you don't want to call the function just to print a value. In most cases, that will not help much. 
Instead, we use the "return" keyword to give back a value.
'''

def say_hello(name="Default"):
    print(f"Hello {name}! How are you?")


say_hello()


def add_two_numbers(num1, num2):
    return num1 + num2

result = add_two_numbers(1,7)

print(result)