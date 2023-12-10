'''
Typically, a function script contains several functions interacting with each other.

'''
from random import shuffle

example_list = [1,2,3,4,5,6,7]

shuffle(example_list)

print(example_list)

def shuffle_list(example_list):
    shuffle(example_list)
    return example_list

example_list=[234234,234,23,4,234,23,42,34,234,23,4,2,4,234,23,42,14,12,4,21534,12]

shuffle_list(example_list)


print("===================================================================================")
print("===================================================================================")
print("===================================================================================")

mylist = [' ', 'O', ' ']

def player_guess():
    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2:   ")

    return int(guess)

def shuffle_ma_list(mylist):
    shuffle(mylist)
    return mylist

def check_guess(guess, mylist):
    if mylist[guess] == "O":
        print("Correct!")
    else:
        print("Incorrect")
        print(mylist)

# initial list
mylist = [' ', 'O', ' ']
# shuffle list
shuffled_list = shuffle_ma_list(mylist)
# have the user guess
guess = player_guess()
# check guess
check_guess(guess, shuffled_list)