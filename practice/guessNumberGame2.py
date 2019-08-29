# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# Ask the player to guess 6 times.
guess = 0
for guessesTimes in range(1, 7):
    print('Take a guess.')

    try:
        guess = int(input())
    except:
        print("You have to input a valid number!")
        continue

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break #This condition is the correct guess!

if guess == secretNumber:
    print('Good jod! You guessed my number in ' + str(guessesTimes) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


