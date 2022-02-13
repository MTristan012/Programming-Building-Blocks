"""
By: Tristan Perea
07 Team Activity
"""

import random

magicNumber = random.randint(1,100)

playGame = input("You want to play? ")
playGame = playGame.lower()
print("What is the magic number? ")
guess = int(input("What is your guess? "))
accountant = 0

while playGame == "yes":
    while magicNumber != guess:
        if magicNumber > guess:
            print("Lower")
            guess = int(input("What is your guess? "))
            accountant = accountant + 1
        else:
            print("Higher")
            guess = int(input("What is your guess? "))
            accountant = accountant + 1
    print("You guessed it! after so " + str(accountant) + " attempst")
    magicNumber = random.randint(1,100)
    accountant = 0
    guess = 0
    playGame = input("You want to coninue playing? ")
    playGame = playGame.lower()

print("Thanks for Play!")


