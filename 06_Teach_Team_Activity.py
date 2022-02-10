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
        elif (firstAgeR >= 12 and firstHeightR >= 52) and (secondAgeR >= 12 and secondHeightR >= 52):
            print("Welcome to the ride. Please be safe and have fun!")
        elif (firstAgeR >= 16 and secondAgeR >= 14) or (firstAgeR >= 14 and secondAgeR >= 16):
            print("Welcome to the ride. Please be safe and have fun!")
        else:
           print("Sorry, you may not ride.")
    else:
       print("Sorry, you may not ride.")
else:
    if firstAgeR >= 18 and firstHeightR >= 62:
        print("Welcome to the ride. Please be safe and have fun!")
    elif (firstAgeR <= 17 and firstAgeR >= 12) and firstHeightR >= 36:
        goldenPass = input("Do You have a Golden Pass? (yes/no)")
        goldenPass = goldenPass.lower()
        if goldenPass == "yes":
            print("Welcome to the ride. Please be safe and have fun!")
        else:
          print("Sorry, you may not ride.")
    else:
        print("Sorry, you may not ride.")