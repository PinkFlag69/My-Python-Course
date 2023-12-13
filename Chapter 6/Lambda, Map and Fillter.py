'''
Lambda functions are ways to create anonymous functions. They are like one time use functions that are used once and then never used again.
You would need to use the map function in python to do this as well as the filter one.

Filter functon allows you to need to filter by a function that returns true or false. 
'''

def square(nums):
    return nums**2

my_nums = [1,4,6,3,9,51,32,12,65]

for item in map(square, my_nums):
    print(item)

print(list(map(square,my_nums)))

def even_check(nums):
    return nums%2 == 0

my_nums2 = [1,2,3,4,5,6,7,8,9,10]

for n in filter(even_check, my_nums2):
    print(n)


# Lambda Function:
lambda num: num**2

for i in map(lambda num: num**2, my_nums2):
    print(i)