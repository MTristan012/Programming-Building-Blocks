"""
By: Tristan Perea
07 Prove Assignment Milestone
"""

from PIL import Image, ImageDraw

#Backgrounds
backgroundBeach = Image.open("07_Prove_Assignment_Milestone_Images/beach.jpg")
backgroundDesert = Image.open("07_Prove_Assignment_Milestone_Images/desert.jpg")
backgroundEarth = Image.open("07_Prove_Assignment_Milestone_Images/earth.jpg")
backgroundField = Image.open("07_Prove_Assignment_Milestone_Images/field.jpg")
backgroundForest = Image.open("07_Prove_Assignment_Milestone_Images/forest.jpg")
backgroundSnowscape = Image.open("07_Prove_Assignment_Milestone_Images/snowscape.jpg")
backgroundSunset = Image.open("07_Prove_Assignment_Milestone_Images/sunset.jpg")

#Green Image
greenBoat = Image.open("07_Prove_Assignment_Milestone_Images/boat.jpg")
greenCactus = Image.open("07_Prove_Assignment_Milestone_Images/cactus.jpg")
greenSmallCat = Image.open("07_Prove_Assignment_Milestone_Images/cat_small.jpg")
greenCat = Image.open("07_Prove_Assignment_Milestone_Images/cat.jpg")
greenHarvester = Image.open("07_Prove_Assignment_Milestone_Images/harvester.jpg")
greenHiker = Image.open("07_Prove_Assignment_Milestone_Images/hiker.jpg")
greenPenguin = Image.open("07_Prove_Assignment_Milestone_Images/penguin.jpg")
greenSpacesHuttle = Image.open("07_Prove_Assignment_Milestone_Images/spaceshuttle.jpg")

#Convert JPG to PNG
greenBoat.save("07_Prove_Assignment_Milestone_Images/boat.png")
greenCactus.save("07_Prove_Assignment_Milestone_Images/cactus.png")
greenSmallCat.save("07_Prove_Assignment_Milestone_Images/cat_small.png")
greenCat.save("07_Prove_Assignment_Milestone_Images/cat.jpg")
greenHarvester.save("07_Prove_Assignment_Milestone_Images/harvester.png")
greenHiker.save("07_Prove_Assignment_Milestone_Images/hiker.png")
greenPenguin.save("07_Prove_Assignment_Milestone_Images/penguin.png")
greenSpacesHuttle.save("07_Prove_Assignment_Milestone_Images/spaceshuttle.png")

print("Image Editor")
print("Marge Images")
print("Select ONE Background: (number)")
print("1.- Beach\n2.-Desert\n3.-Earth\n4.-Field\n5.-Forest\n6.-Snowscape\n7.-Sunset")
backgroundSelector = int(input())
if backgroundSelector == 1:
    backgroundImage = backgroundBeach
elif backgroundSelector == 2:
    backgroundImage = backgroundDesert
elif backgroundSelector == 3:
    backgroundImage = backgroundEarth
elif backgroundSelector == 4:
    backgroundImage = backgroundField
elif backgroundSelector == 5:
    backgroundImage = backgroundForest
elif backgroundSelector == 6:
    backgroundImage = backgroundSnowscape
elif backgroundSelector == 7:
    backgroundImage = backgroundSunset
print("Select ONE Green Image: (number)")
print("1.- Boath\n2.-Cactus\n3.-Small Cat\n4.-Cat\n5.-Harvester\n6.-Hiker\n7.-Penguin\n8.-Spaceshuttle")
greenImageSelector = int(input())
if greenImageSelector == 1:
    greenImage = greenBoat
elif greenImageSelector == 2:
    greenImage = greenCactus
elif greenImageSelector == 3:
    greenImage = greenSmallCat
elif greenImageSelector == 4:
    greenImage = greenCat
elif greenImageSelector == 5:
    greenImage = greenHarvester
elif greenImageSelector == 6:
    greenImage = greenHiker
elif greenImageSelector == 7:
    greenImage = greenPenguin
elif greenImageSelector == 8:
    greenImage = greenSpacesHuttle

greenImageWidth, greenImageHeight = greenImage.size

#Accessing the pixels of the images
greenImagePixel = greenImage.load()
backgroundImagePixel = backgroundImage.load()

#Image inspection
(gIPr, gIPg, gIPb) = greenImagePixel[0, 0]
(bIPr, bIPg, bIPb) = backgroundImagePixel[0, 0]

print(greenImageWidth, greenImageHeight)
print(bIPr, bIPg, bIPb)
print(gIPr, gIPg, gIPb)

newImage = Image.new("RGBA", greenImage.size)
newPixel = newImage.load()

for height in range(0, greenImageHeight):
    for width in range(0, greenImageWidth):
        (r, g, b) = greenImagePixel[width, height]
        (bIPr, bIPg, bIPb) = backgroundImagePixel[width, height]
        if (r >= gIPr and g == gIPg and b >= gIPb):
            newPixel[width, height] = (bIPr, bIPg, bIPb)
        else:
            newPixel[width, height] = (r, g, b)

newImage.show()

flip = input("You Want a Flip the Image? (yes/no) \n")
flip = flip.lower()
if flip == "yes":
    newImage = newImage.transpose(Image.FLIP_LEFT_RIGHT)
    newImage.show()
else:
    print("The Image Will Be Saved Now")
    newImage.save("07_Prove_Assignment_Milestone_Images/NewImage.png")

rotating = input("You Want a Rotate the Image? (yes/no) \n")
rotating = rotating.lower()
if rotating == "yes":
    grades = int(input("how many degrees? (1-359)\n" ))
    newImage = newImage.rotate(grades)
    newImage.show()
else:
    print("The Image Will Be Saved Now")
    newImage.save("07_Prove_Assignment_Milestone_Images/NewImage.png")

message = input("You want to add a Message to the image? (yes/no) \n")
message = message.lower()
if message == "yes":
    textMessage = input("Insert your Mesagge here: \n")
    newImageDraw = ImageDraw.Draw(newImage)
    newImageDraw.text((70,250),textMessage,fill="white")
    newImage.show()
else:
    print("The Image Will Be Saved Now")
    newImage.save("07_Prove_Assignment_Milestone_Images/NewImage.png")


newImage.save("07_Prove_Assignment_Milestone_Images/NewImage.png")
print("Thanks for Use my editor\nYour Image was saved with the name NewImage.png on 07_Prove_Assignment_Milestone_Images")
