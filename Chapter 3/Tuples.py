'''
Tuples are very similar to lists except the fact that they are immutable
This means that they cannot be moved around and is final. 
Tuples use parentheis "()"


You can index and slice with tuples.
You can use the .count() function to count a certain amount of things inside a tuple

Using .index shows the first instance of the input

'''

t = (1, 2, 3)
l = [1, 2, 3]

print(type(t))

tuple1 = ("a", "a", "b", "c")

print(tuple1.count("a"))


print(tuple1.index("a"))





