"""
By: Tristan Perea
06 Team Activity
"""

print("Welcome, please answer the next questions:")

firstAgeRider = int(input("What is the age of the first rider? "))
firstHeightRider = int(input("What is the height of the first rider? "))
secondRider = input("Is there a second rider(yes/no)? ")

secondRider = secondRider.lower()

if secondRider == "yes":
    secondAgeRider = int(input("What is the age of the second rider? "))
    secondHeightRider = int(input("What is the height of the second rider? "))
elif secondRider == "no":
    secondAgeRider = 0
    secondHeightRider = 0

if firstHeightRider >= 36 or secondHeightRider >= 36:
    if (firstAgeRider >= 18 and firstHeightRider >= 62) or (secondAgeRider <= 18 and secondHeightRider >= 62):
        print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
    