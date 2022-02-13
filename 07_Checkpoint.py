"""
By: Tristan Perea
07 checkpoint
"""

positiveNumber = int(input("Please type a positive number: "))

while positiveNumber <= 0:
    print("Sorry, that is a negative number. Please try again.")
    positiveNumber = int(input("Please type a positive number: "))


print("The number is: " + str(positiveNumber))


candy = input("May I have a piece of candy? ")
candy = candy.lower()

while candy != "yes":
    candy = input("May I have a piece of candy? ")
    candy = candy.lower()

print("Thank you.")
