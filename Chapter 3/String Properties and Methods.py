'''
One common strategy is to use string concatenation. It is where you add text to string. 
'''
hello_message = "Hello, world!"
hello_m_updated = hello_message + " It is a beautiful day outside."
print(hello_m_updated)

'''
Another thing you can do is using the .upper and .lower function to make a string upper or lowercase.
Also, there is such thing as the .split function for an input. This can help to split a string into lists.
Leave .split() blank for spaces, and the value you put inside (str, int, etc) will be sorted and then separated, as shown
with the 2023 earning string. 
Tip: Make sure that you add the () to the end of these functions. 
'''

x = "I am cool"
print(x.upper())

y = "Hi this is a string"
list_of_y = y.split()
print(list_of_y)

All_Q_2023_Earnings = "48202,52592,45009,57457"
split_All_Q_2023_Earnings = All_Q_2023_Earnings.split(",")
print(split_All_Q_2023_Earnings)