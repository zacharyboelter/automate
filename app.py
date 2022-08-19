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

dog = ['white', '50lbs', 'blue', 'labradoodle']

color, weight, eyes, breed = dog
print(color)


spam = 42
spam += 1
print(spam)



#~~~ import copy to have immutable list
import copy

spam = ['A', 'B', 1, 2, 3]
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)