"""
By: Tristan Perea
06 checkpoint
"""

print("Please rating from 1 - 10 the next questions:")

largeLoan = int(input("How large is the loan? "))
creditHistory = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
downPayment = int(input("How large is your down payment? "))

desition = bool

if largeLoan >= 5:
    if creditHistory >= 7 and income >= 7:
        desition = True
    elif creditHistory >= 7 or income >= 7:
        if downPayment >= 5:
            desition = True
        else:
            desition = False;
    else:
        desition = False
else:
    if creditHistory < 4:
        desition = False
    else:
        if income >= 7 or downPayment >= 7:
            desition = True
        elif income >= 4 and downPayment >= 4:
            desition = True
        else:
            desition = False

if desition:
    print("YES, Your loan has been approved")
else:
    print("NO, Your loan hasn't been approved")
