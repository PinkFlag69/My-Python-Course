'''
Dictionaries are unordered mappings for storing objects. 
Recently, we saw how lists store in an ordered sequence.
However, dictionaries are key value pairings instead. 

Syntax: {'key1': 'value1', 'key2': 'value2'}

You chose dictionaries if you want something unordered and cannot be sorted.
Lists are for ordered that can be sliced or indexed
Dicts are very versatile and can even store dictionaries and lists inside them
New keyd can also be assigned without directly tampering with the dict. 

One cool function is .keys() function
Opposite is .values()
.items() shows the pairings

'''

prices_lookup = {"cheese": 7.99, "chicken": 10.50, "lettuce": 4.99}
print(prices_lookup["cheese"])

d = {"k1":"value1", "k2": [0, 1, 2, 3, 4], "k3": {"innerk1": 200}}

print(d["k3"]["innerk1"])

e = {"k1": 100, "k2": 200}
e["k3"] =300
print(e["k3"])
print(e.keys())
print(e.values())
print(e.items())