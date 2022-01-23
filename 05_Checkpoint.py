"""
By: Tristan Perea
05 checkpoint
"""

number1 = float(input("What is the first number? "))
number2 = float(input("What is the second number? "))
if number1 > number2:
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
elif number1 == number2:
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
elif number1 < number2:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")
else:
    print("error")
print()
animal = input("What is your favorite animal? ")
animal = animal.lower()
if animal == "owl":
    print("That's my favorite animal too!")
else :
    print("That one is not my favorite.")