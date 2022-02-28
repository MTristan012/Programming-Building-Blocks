"""
By: Tristan Perea
09 Checkpoint
"""
friendsNames = []
newName = ""

while newName != "end":
    newName = input("Type the name of a friend: ")
    friendsNames.append(newName)

friendsNames.pop()
print("Your friends are: ")

for element in friendsNames:
    print(element)