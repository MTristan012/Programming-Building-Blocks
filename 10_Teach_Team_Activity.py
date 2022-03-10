"""
By: Tristan Perea
10 Team Activity
"""
import statistics

items = []
newItem = ""
itemsPrice = []
newPrice = ""

print("Enter the names and balances of bank accounts (type: quit when done) ")
newItem = input("What is the name of this account?: ")
newItem = newItem.capitalize()


while newItem != "Quit":
    items.append(newItem)
    newPrice = float(input(f"What is the price of {newItem}? "))
    newPrice = round(newPrice, 2)
    shopListPrice = str(newPrice)
    itemsPrice.append(shopListPrice)
    newItem = input("What item would you like to add? ")
    newItem = newItem.capitalize()

print("Account Information:")
for counter, (item, itemPrice) in enumerate(zip(items, itemsPrice),  start=1):
    print(f"{counter}. {item} - ${float(itemPrice):.2f}")   

subTotalList = [float(string) for string in itemsPrice]
subTotal = sum(subTotalList)
subAverage = statistics.mean(subTotalList)
print(f"Total: ${float(subTotal):.2f}")
print(f"Average: ${float(subAverage):.2f}")
