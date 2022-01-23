"""
By: Tristan Perea
05 Team Activity
"""

score = int(input("Insert your score here: "))

if score <= 100 and score >= 90:
    grade = "A"
elif score < 90 and score >= 80:
    grade = "B"
elif score < 80 and score >= 70:
    grade = "C"
elif score < 70 and score >= 60:
    grade = "D"
else:
    grade = "F"

if score <= 93 and score > 60:
    scoreSign = score % 10
    if scoreSign >= 7:
        sign = "+"
    elif scoreSign < 7 and scoreSign > 3:
        sign = ""
    elif scoreSign <= 3:
        sign = "-"
else:
    sign = ""

if score >= 60:
    passMessage = " Congratulation you Pass!"
else:
    passMessage = " You Shall not Pass"

print("Your Grade is " + grade + sign + passMessage)