# Strings are charecters between quotation marks 
# Because strings are ordered sequences, it means we can use indexing and slicing to grab sub-sections of the string.
# Indexing notation uses [] notation after the string (or variable assigned to the string) 
# Indexing allows you to grab certain charecters from the string
# Every charecter has an index position. The first charecter starts at 0 and then goes up by an incriment of one. 
# Example: H - E - L - L - O. Index: 0 , 1, 2, 3, 4
# There is also reverse indexing. In the example above it goes: 0, -4, -3, -2, -1
# Slicing allows you to get a subsection of the string.
# This is the syntax: [start:stop:step]
# Start is the numerical index for the slice start
# Stop is the index you will go up to but not include
# Step is the size of the "jump" you will take
print("Hello \nWorld") # The n starts a new line
# Putting t instead of the n above would make it a tab
print("Amount of tax: \t$4000")
# The len function helps you see the length of a function
print(len("Hello World!"))