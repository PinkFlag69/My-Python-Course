# Use for, .split, and if to create a Statement that will only print out words that start with 's'.:

st = 'Print only the words that start with s in this sentence'
newst = st.split()

for word in newst:
    if word[0].lower() == "s":
        print(word)

print("-----------------------")

# Use range() to print all the even numbers from 0 to 10.

for i in range(0,11):
    if i%2 == 0:
        even=True
    else:
        even=False
    if even:
        print(i)

print("-----------------------")
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

for i in range(1,51):
    if i % 3 == 0:
        divisibility = True
    else:
        divisibility = False
    if divisibility == True:
        print(i)

# Or:
print("-----------------------")
divisibility_by_3 = [i for i in range(1,51) if i%3 == 0]
print(divisibility_by_3)

print("-----------------------")

# Go through the string below and if the length of a word is even print "even!"

st2 = 'Print every word in this sentence that has an even number of letters'

st2new = st2.split()

for i in st2new:
    if len(i) % 2 == 0:
        print(i)
    else:
        pass

print("-----------------------")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
print("-----------------------")
# Use List Comprehension to create a list of the first letters of every word in the string below:


st3 = 'Create a list of the first letters of every word in this string'

st3new = st3.split()

newlist = []

for i in st3new:
    newlist.append(i[0])

print(newlist)