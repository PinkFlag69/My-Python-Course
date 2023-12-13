'''
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

def has_33(userimp):
    userimp.append("")
    for i in range(len(userimp)-1):
        if userimp[i] == 3 and userimp[i+1] == 3:
                return True
    
    return False

result = has_33([1,3,4,3,3])

print(result)