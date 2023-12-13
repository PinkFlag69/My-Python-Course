'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(userinput):
    newtext = list(userinput)
    final_return = []
    for i in newtext:
        final_return.append(i*3)
    result = ''.join(final_return)
    print(result)
    return result


paper_doll("I am soo cool")

