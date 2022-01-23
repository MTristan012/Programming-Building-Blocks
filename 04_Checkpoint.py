"""
By: Tristan Perea
04 checkpoint
"""
import math

temperature = int(input("What is the temperature in Fahrenheit? "))
temperature = (temperature - 32) * (5/9)
temperature = round(temperature,1)
print("The temperature in Celsius is " + str(temperature) + " degrees.")