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
        for counter, (item, itemPrice) in enumerate(zip(items, itemsPrice),  start=1):
            print(f"{counter}. {item} - ${float(itemPrice):.2f}")
            #print(str(counter) +". " + item + " - $" +"{:.2f}".format(float(itemPrice)))
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
        print(
            f"The total price of the items in the shopping cart is ${float(subTotal):.2f}")
        selector = input("Do you want to finish your purchase? (yes/no): ")
        selector = selector.capitalize()
        if selector == "Yes":
            taxesrate = float(input("What is the sales tax rate? "))
            taxes = subTotal/(100/taxesrate)
            taxes = round(taxes, 2)
            print(f"Sales Tax: ${float(taxes):.2f}")
            total = subTotal + taxes
            total = round(total, 2)
            print(f"Total: ${float(total):.2f}")
            print("Please enter the following information: ")
            name = input("First Name: ")
            lastName = input("Last Name: ")
            email = input("Email Address: ")
            phonenumber = input("Phone Number: ")
            card = input("Credit Card Number: ")
            address = input("Address: ")
            print("Your Ticket: ")
            print("--------------------------------------------------")
            print(lastName.upper() + ", " + name.capitalize())
            print(email.lower())
            print(phonenumber)
            print(f"Total: ${float(total):.2f}")
            print("Your purchase will arrive at the following address: " + address)
            print("--------------------------------------------------")
            break
        else:
            print("Returning to the main menu")
    print()
    print("Please select one of the following: ")
    print("1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")
    action = int(input("Please enter an action: "))

print("Thank you. Goodbye.")
