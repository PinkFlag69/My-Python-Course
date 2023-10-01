'''
Sets are unordered collections of unique elements. 
This means that there can only be one representative of the same object. 



'''

myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
print(myset)

mylist = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,6,6,4,5,5,5,3,2,2,4,6,7,7,8,4,4,3,3,2,3]
print(set(mylist))