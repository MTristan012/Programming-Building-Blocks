"""
File: Prove Milestone - Meal Price Calculator
Author: MTristan Perea

"""
#Global Variables for extra challenge
npersons = int
soda = float
dessert = float

#In float variable I save the price for meal
childprice = float(input("What is the price of a child's meal? "))
adultprice = float(input("What is the price of an adult's meal? ")) 

#In Int variable I save the number of persons
nchildren = int(input("How many children are there? "))
nadults = int(input("How many adults are there? "))
npersons = nchildren + nadults  # Calculate for Extra Challenge

#Extra Challenge
sodarequest = input("Do you want Soda for every meal?: ")
sodarequest = sodarequest.lower()
sodacost = float(input("What is the price of a soda? "))
if sodarequest == "yes":
    soda = npersons * sodacost
elif sodarequest == "no":
    soda == 0
else:
    print("Incorrect Answer")
    soda == 0
dessertrequest = input("Do you want Dessert for every meal?: ")
dessertrequest = dessertrequest.lower()
dessertcost = float(input("What is the price of a dessert? "))
if dessertrequest == "yes":
    dessert = npersons * dessertcost
elif dessertrequest == "no":
    dessert == 0
else:
    print("Incorrect Answer")
    dessert == 0

#In float variable I save the sales taxe rate
taxesrate = float(input("What is the sales tax rate? "))
#In subtotal I save the valor without taxes
subtotal = (childprice * nchildren) + (adultprice * nadults) + soda + dessert
subtotal = round(subtotal,2)
print()
print("Subtotal: $" + str(subtotal))

#Here calculate the taxes
taxes = subtotal/(100/taxesrate)

#Here round the valor of taxes
taxes = round(taxes,2)
print("Sales Tax: $" + str(taxes))

#Here plus the valor of taxes and the valor of subtotal and round
total = subtotal + taxes
total = round(total,2)
print("Total: $" + str(total))
print()
paymentamount = int(input("What is the payment amount? "))

#Here rest the total about the payment
change = paymentamount - total
change = round(change,2)
print("Change: $" + str(change))
print()
print("Enjoy your Meal!!")
