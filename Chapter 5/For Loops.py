'''
Many objects in python are iterable, meaning that we can iterate over every element in the object. 
We can use for loops to execute a block of code for every iteration.
The term iterate means to repeat something.

Syntax:
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
'''

mydata = "Hello!"
for i in mydata:
    print(i)

# This is an example of tuple unpacking. 
mylist = [(1,3), (4,17), (14,3), (6,8)]
for (a,b) in mylist:
    print(a)
    print(b)

# By default, when you iterate through a dict, it iterates the keys
myDict = {"k1":1, "k2":2, "k3":3}
for i in myDict:
    print(i)
# if you want to print the items and keys do this:
for i in myDict.items():
    print(i)
# Similarily, .values will do the same but with the end values, though I can't be fucked to type it out