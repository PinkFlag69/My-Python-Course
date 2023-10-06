'''
Control flow:
In our programs, we often want certain conditions to be met before certain code runs.
For example, if my dog was hungry then -> I'd feed my dog.

To control this flow of logic we use some keywords:
* If
* Elif
* Else

Control flow syntax makes use of colons and indentation (whitespace).

Basic syntax:
if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else:
    # do something else

You can have many elifs. 

'''

hungry = False

if  hungry:
    print("I'm hungry! >:(")
else:
    print("I'm not hungry >:)")

