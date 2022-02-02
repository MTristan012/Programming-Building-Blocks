"""
By: Tristan Perea
05 Prove Milestone - Adventure Game
"""

def start_adventure():
    print("On the fourth age of the blood moon." +  
    "\n" + "A stranger driven by hunger and despair drives him away from the refuge...")
    print("You are this stranger...")
    print()
    item = input("You are walking through a dark forest and find two items: " +
                 "\n" + "a MATCH and a FLASHLIGHT." + 
                 "\n" + "Which one do you want to pick up? ")
    print()
    item = item.upper()
    if item == "MATCH":
        desition1 = input("You pick up the MATCH and strike it, and for an instant, the forest around you is illuminated." +
                          "\n" + "You see a large grizzly bear, and then the match burns out." + 
                          "\n" + "Do you want to RUN, or HIDE behind a tree? ")
        print()
        desition1 = desition1.upper()
        if desition1 == "RUN":
            desition2 = input("You RUN, The bear driven by a hunger greater than yours runs after you." + 
                              "\n" + "Do you RUN until you reach a river, the bear comes after you," + 
                              "\n" + "do you SWIM or TAKE a rock to defend yourself? ")
            desition2 = desition2.upper()
            print()
            if desition2 == "SWIM":
                print("You enter the river to swim and the force of this takes you away from the bear, \nyou are safe from being devoured, \nbut now you cannot get out of the river, \nyour destiny has become uncertain.")
            elif desition2 == "TAKE":
                print("You TAKE a river stone, ready to defend yourself, \nthe bear stands on two legs and lets out a loud roar, \nyou await your end when a roar greater than that of the bear freezes your blood, \nthe bear gets scared and runs away , You should do the same.")
            else:
                print("Incorrect Answer")
        elif desition1 == "HIDE":
            desition2 = input("You quickly drop the match and climb a tree." + 
                            "\n" + "The bear begins to smell the surroundings, it knows that there is someone nearby," + 
                            "\n" + "it detects your aroma and turns up, after a loud roar it begins to hit the tree so that you fall," +
                            "\n" + "next to you you see another tree, what do you do JUMP or STAY?. ")
            desition2 = desition2.upper()
            print()
            if desition2 == "JUMP":
                print("You JUMP, you manage to reach the other tree, \nthe bear approaches the tree where you jumped but from the bushes, a rabbit runs out and the bear chases it, \nyour legs and arms are shaking too much to go down, but at least you are safe.")
            elif desition2 == "STAY":
                print("You STAY, the tree starts to crack, \nthe tree will soon fall, when you feel that all is lost, \na friend from the camp appears with a torch and scares the bear, \nhelps you down and takes you back to the camp.")
        else:
            print("Incorrect Answer")
    elif item == "FLASHLIGHT":
        desition1 = input("You pick up the flashlight and turn it on."+ 
                        "\n" +"You see the pathway lit up in front of you, but you thought you also heard something off to the side." + 
                        "\n" + "Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
        desition1 = desition1.upper()
        print()
        if desition1 == "FOLLOW":
            desition2 = input("You FOLLOW the path, the sound has been left behind," + 
                        "\n" + "You go further into the forest, you begin to feel observed and the batteries of the flashlight run out," + 
                        "\n" + "You SHOUT for help or KEEP silent? ")
            desition2 = desition2.upper()
            print()
            if desition2 == "SHOUT":
                print("You SHOUT for help, but only hear your echo rumble through the forest. \nYou are cold and the hunger has not stopped, you start to hear murmurs around you, you were found, but not by who you expected.")
            elif desition2 == "KEEP":
                print("You KEEP in silent, you are prudent, \nYou know that there are things out there with you that are more dangerous than a bear, \n you see a wonderful moon among the clouds, \n but when its color turns red, you know it is time to hide.")
            else:
                print("Incorrect Answer")
        elif desition1 == "LOOK":
            desition2 = input("You LOOK for the cause of the noise, you discover a small rabbit feeding on a berry," + 
                        "\n "+"the rabbit looks at you and runs away, you take some berries and what do you do? " + 
                        "\n" + "Are you going BACK to camp or do you WANT to catch the rabbit for a bigger dinner? ")
            desition2 = desition2.upper()
            print()
            if desition2 == "BACK":
                print("You return to the camp, the lookout inspects you and allows you to enter, \nyou share the berries you brought, while you enjoy eating, you hear a loud roar in the distance, \n that reminds us that we are not alone.")
                print()
            elif desition2 == "WANT":
                print("You want to catch the rabbit, you haven't tasted the meat for a long time, \nyou look for the rabbit's trail and you go further into the forest, you hear a screech, \n something caught the rabbit and it wasn't you, \n your hunger can now be the end of you.")
                print()
            else:
                print("Incorrect Answer")
        else:
            print("Incorrect Answer")
    else:
        print("Incorrect Answer")

def exit():
 print("See you later adventurer")

print("Welcome Adventurer")
print("A) Start The Adventure B) Exit")
modeSelect = input()
print()
modeSelect = modeSelect.upper()
if modeSelect == "A":
    start_adventure()
elif modeSelect == "B":
    exit()
else:
    print("Incorrect Answer")