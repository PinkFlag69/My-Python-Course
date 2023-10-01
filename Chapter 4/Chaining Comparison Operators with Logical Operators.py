'''
We can chain together operators using:
* and
* or
* not

And requires all conditions to be true
Or requires one of the conditions to be true
Not returns the opposite boolean of the expression

Some people like to wrap these parts in parenthesis for readability. 
'''

# And
test1 = 1 > 2 and 2 > 3
print(test1)
# Or
test2 = 1 == 2 or 3 == 3
print(test2)
# Not
test3 = not (1==2 or 3==3)
print(test3)