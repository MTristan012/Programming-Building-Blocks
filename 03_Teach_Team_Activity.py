"""
File: Team Activity
Author: MTristan Perea

"""
import math

#Area and Volume
ssquare = int(input("What is the length of a side of the square? "))
print()
asquare = ssquare * ssquare
vsquare = asquare * ssquare
print("The area of the square is: " + str(asquare) + " squere centimeters")
print("The area of the square is: " + str(asquare/10000) + " squere meters")
print("The volume of the cube is " + str(vsquare))
print()

#Area and Volume
lrectangle = int(input("What is the length of rectangle? "))
wrectangle = int(input("What is the width of the rectangle? "))
hrectangle = int(input("What is the high of the rectangular prism? "))
print()
arectangle = lrectangle * wrectangle
vrectangle = arectangle * hrectangle
print("The area of the rectangle is: " + str(arectangle) + " squere centimeters")
print("The area of the rectangle is: " + str(arectangle/10000) + " squere meters")
print("The volume of the cube is " + str(vrectangle))
print()

#Area and Volume
cradius = int(input("What is the radius of the circle? "))
print()
acircle = math.pi * (cradius**2)
acircle = round(acircle,2)
vcircle = 4/3 * math.pi * (cradius**3)
vcircle = round(vcircle,2)
print("The area of the circle is: " + str(acircle) + " squere centimeters")
print("The area of the circle is: " + str(acircle/10000) + " squere meters")
print("The volume of the sphere is " + str(vcircle))