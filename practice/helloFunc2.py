import random

def getAnswer(number):
    if number == 1:
        return 'It is certain'
    elif number == 2:
        return  "It is decidely so"
    elif number == 3:
        return  "Yes"
    elif number == 4:
        return  'Reply hazy try again'
    elif number == 5:
        return 'Ask again later'
    elif number == 6:
        return 'Concentrate and ask again'
    elif number == 7:
        return "My reply is no"

for i in range(0, 11):
    r = random.randint(1, 7)
    answer = getAnswer(i)
    if answer == None:
        print("This is a None")

