'''
Returning will basically end the program. Hence, indentation is very important
'''


def is_it_even_or_odd(odd_or_even_input):
    '''
    This is a simple function to check if a number is odd or even. First of all, it flows that input into a verification process. It turns it into an integer and trips the white space. Then, it does the usual modulus function to determine Odd or Even value.
    '''
    newnum = int(odd_or_even_input)
    if newnum % 2 == 0:
        return("Even")
    else:
        return("Odd")
    

result = is_it_even_or_odd(21)
print(result)


def check_even_list(num_list):
    for i in num_list:
        if i % 2 == 0:
            return True
        else:
            pass
    return False
        
print(check_even_list([1,2,3]))