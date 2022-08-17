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


import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')
pyperclip.paste()