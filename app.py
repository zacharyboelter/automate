# while loop

# name = ''
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break                               #break statement so the infinite loop will close out
# print('Thank you')    

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('Spam is ' + str(spam))