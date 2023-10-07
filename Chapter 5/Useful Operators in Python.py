'''
Range:
Range is a built in feature because people were typing in list for so much time.
Just like slicing, it goes up to but not including the range. 
Ranges, like slices have steps, a start and a middle
It goes range(start,stop,step)
Not only this, but you can cast this range into lists.

Enumerate:
The enumerate function can help you keep a "counter" in your Python code.

Zip Function:
This will combine iterables (lists, tuples, etc). You need to iterate through it to get the actual concents. 
If the input iterables are of different lengths, zip will stop creating pairs when the shortest iterable is exhausted

In:
The in keyword is a good way to check if something is in another thing. It can be lists, dicts,etc.  It is quick and sharp. 

Min and Max:
Keywords to find the minimum value of something. min() is how to do it. 

From:
Allows you to import libraries with custom functions

Input:
Allows you to take in user inputs

'''
# Range
for i in range(-50,100,5):
    print(i)

nums = range(0,100,10)
mylist = list(nums)
print(mylist)

# Without enumerate:
index_position = 0
for letter in "abcdefgh":
    print(f"At index position {index_position}, there is letter {letter}")
    index_position += 1

# With enumerate:
for letter in enumerate("abcdefghijk"):
    print(letter)

# Zipping
num1 = [1,2,3,4,5]
letter1 = ["a", "b", "c", "d", "e"]
words1 = ["Hello", "my", "name", "is", "chicka", "chika", "Slim", "Shady"]
for items in zip(num1, letter1, words1):
    print(items)

# In
condition = 'x' in ['x', 'y', 'z']
print(condition)

# From
from random import shuffle
mylist2 = [1,2,3,4,5,6,7,8,9,10]
print(shuffle(mylist2))

