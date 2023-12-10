def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2


result = lesser_of_two_evens(2,5)

print(result)