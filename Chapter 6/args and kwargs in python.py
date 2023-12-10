'''
*args and **kwargs

They stand for arguments and key word arguments


In the example below, it just takes a and b and returns 5 percent of their sum. the question that arises is - what if we want to tae in more values? In the example, a and b are known as positional arguments. That means that 40 was assigned to a because it was in the first position and 60 is assigned to b because it was in the second position. 

By default, the parameters you put into *args becomes a tuple

Keep in mind, the star/s itself is all that is necessary. args or kwargs is just an artbitrary term that is not necessarily needed. it could infact be *spam or **poop if you want to! However, by convention, you should use args and kwargs if someone else is viewing the code

Keyword arguments works in a similar way, except that it gives back as a dictionary
'''

def myfunc(a,b):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

result = myfunc(40,60)
print(result)

# New function

def myfunc2(*args):
    result = sum(args)* 0.05
    print(result)
    return result

myfunc2(100,200,300,400,500,600,700,800,900,1000)

def myfunc3(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit in here")

myfunc3(fruit="apple", veggie="letuce")

def combinationfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}!".format(args[0], kwargs.get("food", "")))

combinationfunc(11, 3, 2, 32, 34, 234, food="eggs", animal="kitten", vegetable="cucumber")

