"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"
"""


def master_yoda(text):
    lowecase = text.lower()
    newtext = lowecase.split()
    newtext2 = newtext[::-1]
    finale = " ".join(newtext2)
    finale_actually = finale[0].upper() + finale[1::]
    return finale_actually

result = master_yoda("I love apples and pears because they are so juicy")
print(result)