"""
By: Tristan Perea
09 Prove Assignment Milestone
"""

items = []
newItem = ""
itemsPrice = []
newPrice = ""

print("Please select one of the following: ")
print("1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")
action = int(input("Please enter an action: "))

while action != 5:
    if action == 1:
        newItem = input("What item would you like to add? ")
        newPrice = float(input(f"What is the price of {newItem}? "))
        shopList = newItem.capitalize()
        newPrice = round(newPrice, 2)
        shopListPrice = str(newPrice)
        items.append(shopList)
        itemsPrice.append(shopListPrice)
        print(f"{newItem} has been added to the cart.")
    elif action == 2:
        print("The contents of the shopping cart are: ")
        for counter,(item, itemPrice) in enumerate(zip(items, itemsPrice),  start=1):
                print(f"{counter}. {item} - ${itemPrice}")
    elif action == 3:
        remove = int(input("Which item would you like to remove?: "))
        remove = remove - 1
        removeList = items[remove]
        removeListPrice = itemsPrice[remove]
        items.remove(removeList)
        itemsPrice.remove(removeListPrice)
        print("Item Removed")
    elif action == 4:
        subTotalList = [float(string) for string in itemsPrice]
        subTotal = sum(subTotalList)
        print(f"The total price of the items in the shopping cart is ${subTotal}")
        
    print()
    print("Please select one of the following: ")
    print("1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")
    action = int(input("Please enter an action: "))

print("Thank you. Goodbye.")
