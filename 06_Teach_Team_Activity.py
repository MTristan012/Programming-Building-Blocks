"""
By: Tristan Perea
06 Team Activity
"""

firstAgeR = int(input("What is the age of the first rider? "))
firstHeightR = int(input("What is the height of the first rider? "))
secondRider = input("Is there a second rider (yes/no)? ")
secondRider = secondRider.lower()
if secondRider == "yes":
   secondAgeR = int(input("What is the age of the second rider? "))
   secondHeightR = int(input("What is the height of the second rider? "))
   if firstHeightR >= 36 and secondHeightR >= 36:
       if firstAgeR >= 18 or secondAgeR >= 18:
           print("Welcome to the ride. Please be safe and have fun!")
       else:
           print("Sorry, you may not ride.")
   else:
       print("Sorry, you may not ride.")
else:
    if firstAgeR >= 18 and firstHeightR >= 62:
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")