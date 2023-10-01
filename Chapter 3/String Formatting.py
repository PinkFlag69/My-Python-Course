'''
You can format strings the first way: .format
You add {} at certain postions in the string
You can add them multiple times. You can also index them.
You can add them in any place you want. 
Do [any assignment]="string" inside the .format to get "keywords" 
'''

print("This is a string {}".format("INSERTED"))

print("I really like {1}{3}{0}{2}".format("it's ", "cheese ", "yummy.", "because "))
print("What is the {} of the universe?".format("meaning"))
print("When the {going} get's rough, the {rough} get going.".format(going="going", rough="rough"))

# Float formatting follows {value:width.precision f}
result = 100/69
print("The result is: {r:1.5f}".format(r=result))

'''
The other way is using f-string. Similar concept, just easier. 
Can be done will multiple variables in the same way you can with the first method. 
'''

typeof_chocolate = "almond"
status = "currently"

print(f"I'm {status} eating {typeof_chocolate} chocolate!")

