"""
By: Tristan Perea
13 Prove Assignment Milestone
"""

def temperatureCalculator(fOrC):

    winchillCard = open("WinchillCard.txt", "w")

    if fOrC == "C":
        cToF = farenheit(temperature)
        for i in range(5,65,5):
            winchill = 35.74 + (0.6215 * cToF) - 35.75 * (i**0.16) + (0.4275*cToF*(i**0.16))
            print(f"At temperature {cToF:.1f}F, and wind speed {i} mph, the windchill is: {winchill:.2f}F")
            winchillCard.write(f"At temperature {cToF:.1f}F, and wind speed {i} mph, the windchill is: {winchill:.2f}F\n")
    elif fOrC == "F":
        for i in range(5,65,5):
            winchill = 35.74 + (0.6215 * temperature) - 35.75 * (i**0.16) + (0.4275*temperature*(i**0.16))
            print(f"At temperature {temperature:.1f}F, and wind speed {i} mph, the windchill is: {winchill:.2f}F")
            winchillCard.write(f"At temperature {temperature:.1f}F, and wind speed {i} mph, the windchill is: {winchill:.2f}F\n")
    return winchill

def farenheit(temperatura):
    celciusToF = (temperature*(9/5))+32
    return celciusToF

temperature = int(input("What is the temperature? "))
fOrC = input("Fahrenheit or Celsius (F/C)? ").upper()

temperatureCalculator(fOrC)

print("This information was saved in a txt file")
