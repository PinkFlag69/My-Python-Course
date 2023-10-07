'''
List comprehention is a unique way of quickly creating a list in python. 
It is a good alternative to using a for loop and using .append()
Essentially, the logic is a flattened out for loop.
In the first example of list comprehension, the variable, in this case letter, needs to be done two times.
Eg. it needs to be letter for letter, not i for letter or letter for i for example. 
You can also do it in ranges and can also preform operations to the first variable
You can also use an if statement at the end of the list comprehension to add some conditions.
You can also use an else statement in it. 
If you're using an if in list comprehension, then it is at the end, but if you're using it with if and else
then it is at the start

Remember to prioritise readability over simplicity

'''

# How it is usually done:
mystring = "hello"
mylist = []
for charecter in "hello!":
    mylist.append(charecter)
print(mylist)

# First example of list comprehension
mynewlist = [letter for letter in mystring]
print(mynewlist)

# Using ranges

mynumlist = [num**0.5 for num in range(0,11)]
print(mynumlist)

mynewnumlist = [num**2 for num in range(0,11) if num%2==0]
print(mynewnumlist)

results = [x if x%2==0 else "ODD" for x in range(0,11)]
print(results)