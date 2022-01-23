"""
By: Tristan Perea
04 Team Activity
"""

import math

#Constants
g = 9.8
gJupiter = 24

print("Welcome to the velocity calculator. Please enter the following: ")
print()
m = int(input("Mass (in kg): "))
t = int(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))

#Extra Challenge In this part I give more option to drag coefficient 
print("Drag Coefficient")
C = input(" a) 0.47 for sphere b) 0.42 for half-sphere c) 0.5 for cone d) 1.05 for cube e) 0.8 for angle cube f) 0.82 for long cylinder g) 1.15 for short cylinder h) 0.04 for Streamlined body i) 0.09 for Streamlined half-body: ")
C = C.lower()
if C == "a":
    C = round(0.47,1)
elif C == "b":
    C = round(0.42,1)
elif C == "c":
    C = 0.50
elif C == "d":
    C = 1.05
elif C == "e":
    C = round(0.80,2)
elif C == "f":
    C = round(0.82,2)
elif C == "g":
    C = round(1.15,2)
elif C == "h":
    C = 0.04
elif C == "i":
    C = 0.09
else:
    print("Invalid Answer... Sphere valor is now default")
    C = round(0.47, 1)
print("In case for more specific Drag Coefficient is necessary work in .ipynb files")
print()

#Math Operation
c = (1 / 2) * p * A * C #Inner Valor of c
c = round(c,3)
v = math.sqrt((m*g)/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t)) #Equation for Velocity after #time
v = round(v,3)
vTerminal = math.sqrt((2*m*g)/(C*p*A)) #Equation for terminal velocity
vTerminal = round(vTerminal,3)

#Print the results
print("The inner value of c is: " + str(c))
print("The velocity after " + str(t) + " seconds is: " + str(v) + " m/s on Earth")
print("The terminal Velocity is " + str(vTerminal) + " m/s on Earth")
print()

#Extra Challenge
v = math.sqrt(m*gJupiter/c) * (1 - math.exp((-math.sqrt(m*gJupiter*c)/m)*t)) #Equartion for Velocity after #time
v = round(v,3)
#Print the results
print("The velocity after " + str(t) + " seconds is: " + str(v) + " m/s on Jupiter")
print()