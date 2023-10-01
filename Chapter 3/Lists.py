'''
Lists are an ordered sequence that can hold a few data types
They use square [] brackets to separate objects in the list. 
They can also be indexed and sliced
'''

my_list = [1, "Cheese", 3.1415]
print(len(my_list))
# You can also change certain values in lists
my_list[0] = 2
print(my_list)

# You can use .append to add values and .pop to do the opposite

my_list.append("Hello world")
print(my_list)

new_list = [19, 20, 21, 22, 23]
new_list.pop()
print(new_list)
# This is not limited to just the end of the list, it can be anywhere by using indexing.
new_list.pop(0)
print(new_list)

alpha_list = ["a", "b", "z", "e", "c", "f", "x"]
alpha_list.sort()
print(alpha_list)


# .sort sorts the list based on alpha-numeric sorting. Works for charecter and numbers
new_alpha_List =['abc', 'cba', 'abe', 'oab', 'obe', 'oaa']
new_alpha_List.sort()
print(new_alpha_List)
# Reverse.... reverses the list
new_alpha_List.reverse()
print(new_alpha_List)