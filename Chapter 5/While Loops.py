'''
While loops will execute code while some condition remains true.

Syntax:

while some_condition:
    # do another thing

This can be combined with else, else if, etc.

'''
x = 1
while x < 100:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("")

'''
We can use break, continue and pass for extra functionality. 
break: close the current closest enclosing loop.
continue: Goes to the top of the closest enclosing loop.
pass: does nothing at all

'''