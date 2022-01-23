"""
By: Tristan Perea
05 Prove Milestone - Adventure Game
"""

print("On the fourth age of the blood moon, a stranger driven by hunger and despair drives him away from the refuge...")
print("You are this stranger...")
item = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")
item = item.upper()
if item == "MATCH":
    desition1 = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")
    desition1 = desition1.upper()
    if desition1 == "RUN":
        desition2 = input("The bear driven by a hunger greater than yours runs after you.")
        desition2 = desition2.upper()
    elif desition1 == "HIDE":
        desition2 = input("You quickly drop the match and climb a tree, the bear begins to smell the surroundings, it knows that there is someone nearby, it detects your aroma and turns up, after a loud roar it begins to hit the tree so that you fall, next to you you see another tree, what do you do JUMP or STAY?. ")
        desition2 = desition2.upper()
    else:
        print("Incorrect Answer")
elif item == "FLASHLIGHT":
    desition1 = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
    desition1 = desition1.upper()
    if desition1 == "FOLLOW":
        desition2 = input()
        desition2 = desition2.upper()
    elif desition1 == "LOOK":
        desition2 = input()
        desition2 = desition2.upper()
    else:
        print("Incorrect Answer")
else:
    print("Incorrect Answer")