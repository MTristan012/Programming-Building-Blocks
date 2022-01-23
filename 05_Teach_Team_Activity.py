"""
By: Tristan Perea
05 Team Activity
"""

score = int(input("Insert your score here: "))

if score <= 100 & score >= 90:
    print("Your grade is A")
elif score < 90 & score >= 80:
    print("Your grade is B")
elif score < 80 & score >= 70:
    print("Your grade is C")
elif score < 70 & score >= 60:
    print("Your grade is D")
elif score < 60:
    print("Your grade is F")
else:
    print("score not valid")