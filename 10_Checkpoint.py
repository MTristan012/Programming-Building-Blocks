"""
By: Tristan Perea
10 Checkpoint
"""
shopList = []
newItem = ""

print("Please enter the items of the shopping list (type: quit to finish) ")
newItem = input("Item: ")


while newItem != "Quit":
    newItem = input("Item: ")
    newItem = newItem.capitalize()
    shopList.append(newItem)

shopList.pop()

print()
print("The shopping list is:")
for item in shopList:
    print(item)

print()
print("The shopping list with indexes is:")
for counter, item in enumerate(shopList, start=1):
    print(f"{counter}. {item}")

change = int(input("Which item would you like to change? "))
change = change -1
replaceItem = input("What is the new item? ")
replaceItem = replaceItem.capitalize()
shopList[change] = replaceItem

print()
print("The new shopping list with indexes is:")
for counter, item in enumerate(shopList, start=1):
    print(f"{counter}. {item}")
