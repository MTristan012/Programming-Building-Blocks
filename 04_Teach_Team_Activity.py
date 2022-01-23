"""
By: Tristan Perea
04 Team Activity
"""

import math

print("Welcome to the velocity calculator. Please enter the following: ")
print()
m = int(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = int(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()
c = (1 / 2) * p * A * C
c = round(c,3)
v = math.sqrt(m*g/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))
v = round(v,3)
print("The inner value of c is: " + str(c))
print("The velocity after " + str(t) + " seconds is: " + str(v) + " m/s")