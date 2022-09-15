# while loop

# name = ''
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break                               #break statement so the infinite loop will close out
# print('Thank you')    

# spam = 0
# while spam < 5:
#     spam = spam + 1
#     if spam == 3:
#         continue    #continue statement will skip over 3 while printing the rest
#     print('Spam is ' + str(spam))

# for loop

# total = 0
# for num in range(101):
#     total = total + num
# print(total)



# import random

# random_num = random.randint(0, 10000)
# print(random_num)


#functions

# def hello():
#     print('howdy')
#     print('hello world')

# hello()
# hello()
# hello()
# hello()

# import random

# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It certainly is'
#     elif answerNumber == 2:
#         return 'It is decidedly so.'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy, try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My answer is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'

# print('Think of a question to ask me.')
# input()

# print(getAnswer(random.randint(1, 9)))


# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: You tried to divide by zero!')


# print(div42by(2))
# print(div42by(10))
# print(div42by(0))
# print(div42by(1))


# import random
# print('What is your name?')
# name = input()
# secretNumer = random.randint(1, 20)
# print(f'Hello {name}, I am think of a number between 1 and 20')

# # set the number of guesses to 6
# for guessesTaken in range(1, 7):
#     print('Take a guess')
#     guess = int(input()) 
#     if guess < secretNumer:
#         print('That number is too low, guess again.')
#     elif guess > secretNumer:
#         print('That number is too high, try again')
#     else:
#         break #this is the correct guess, break out of loop
   

# # closing message

# if guess == secretNumer:
#     print(f'That was it {name}! The number was {str(secretNumer)} and it only took you {str(guessesTaken)} guesses. Great job.')
# else:
#     print(f'So sorry {name}, the number was {str(secretNumer)}')



# Functions with lists 
# ~~~~For loop~~~~~~

# supplies = ['pens', 'scissors', 'paper', 'water', 'computers', 'phones', 'notebooks']

# for i in range(len(supplies)):
#     print(f'Index: {i}. Item: {supplies[i]}')


# ~~~~~Multiple Assignment ~~~~~~~~

# dog = ['white', '50lbs', 'blue', 'labradoodle']

# color, weight, eyes, breed = dog
# print(color)


# spam = 42
# spam += 1
# print(spam)



# #~~~ import copy to have immutable list
# import copy

# spam = ['A', 'B', 1, 2, 3]
# cheese = copy.deepcopy(spam)
# cheese[1] = 42
# print(cheese)
# print(spam)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  DICTIONARIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# myDog = {
#     'size': 'athletic',
#     'color': 'white and brown',
#     'dispostion': 'good boi'
# }

# eggs = {'name': 'bill', 'age': '3', 'color': 'blue'}
# ham = {'age': '3', 'name': 'bill', 'color': 'blue'}

# # print(eggs == ham)               #dictionaries are unordered

# 'name' in eggs                  #true   
# 'name' not in ham               #false

# 'dob' in eggs                   #key error  

#~~~~~~ Dictionary Methods ~~~~~~~~~~~

# print(list(eggs.keys()))
# print(list(eggs.values()))
# print(list(eggs.items()))

# for k in eggs.keys():
#     print(k)

# for v in eggs.values():
#     print(v)

# for k, v in eggs.items():
#     print(k, v)

# for i in eggs.items():
#     print(i)

# print(eggs.get('milk', 0))      #get the milk key, otherwise return 0
# print(eggs.get('age', 10))      #get the age key, otherwise return 10

# #~~~~~~~~ SetDefault ~~~~~~~~

# # if 'species' not in eggs:
# #     eggs['species'] = 'dog'

# eggs.setdefault('species', 'elephant')          #if no 'species' key value pair, then make one and set it this this.

# print(eggs)




#~~~~~~~~~~~~~~~~~ Character Count ~~~~~~~~~~~~~~~~

import pprint

# message = '''When I die I want your hands on my eyes:
# I want the light and the wheat of your beloved hands
# to pass their freshness over me one more time
# to feel the smoothness that changed my destiny.

# I want you to live while I wait for you, asleep,
# I want for your ears to go on hearing the wind,
# for you to smell the sea that we loved together
# and for you to go on walking the sand where we walked.

# I want for what I love to go on living
# and as for you I loved you and sang you above everything,
# for that, go on flowering, flowery one,

# so that you reach all that my love orders for you,
# so that my shadow passes through your hair,
# so that they know by this the reason for my song.'''
# count = {}

# for character in message.upper():
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# pprint.pprint(count)


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard) 

