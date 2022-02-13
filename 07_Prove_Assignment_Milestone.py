"""
By: Tristan Perea
07 Prove Assignment Milestone
"""

from PIL import Image

#Backgrounds
backgroungBeach = Image.open("07_Prove_Assignment_Milestone_Images/beach.jpg")
backgroungDesert = Image.open("07_Prove_Assignment_Milestone_Images/desert.jpg")
backgroundEarth = Image.open("07_Prove_Assignment_Milestone_Images/earth.jpg")
backgroungField = Image.open("07_Prove_Assignment_Milestone_Images/field.jpg")
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

imageCombined = Image.new("RGB", greenBoat.size)
(width, height) = greenBoat.size


pixelsBoat = greenBoat.load()

for y in range(0, height):
    for x in range(0, width):
        (r, g, b) = pixelsBoat[x, y]
        pixelsBoat[x, y] = (r, 0, b)

backgroungBeach.paste(greenBoat, (0, 0),)

backgroungBeach.show()


"""
width, height = greenBoat.size
pixelsBoat = greenBoat.load()
r, g, b = pixelsBoat[100,200]

#Clean Green Screen
pixelsBoat[100,200] = (r,g,b)

imageNew = Image.new("RGB", greenBoat.size)
pixelsNew = imageNew.load()

pixelsNew[100,200] = (r,g,b)

imageNew.show()
"""
