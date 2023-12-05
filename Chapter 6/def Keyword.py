'''
Creating a function in python requires a specific syntax, including the **def** keyword, correct indentation and correct structure. 


Example:

def name_of_function():

It uses snake casing. This is where every word is separated with an underscore as each word begins with a lowercase word. 
    <<<Optional Docstring to explain the function>>> You use the triple apostrphe to do so.

    
Typically, we use the return keyword to send back the result of the function, instead of just printing it out.
Return allows us to assign the output of the function inside a varaible.
'''

# Functions can accept parameters. These can then be used inside the function. In this example, the parameters are name.
def say_hello(name):
    print("Hello! You are a pretty cool person " + name)

say_hello("Dario")