"""
By: Tristan Perea
11 Prove Assignment Milestone
"""
import pandas as pd

masterList = pd.read_csv("life-expectancy.csv", delimiter=",")

entity = masterList.loc[:, "Entity"]
code = masterList.loc[:, "Code"]
years = masterList.loc[:, "Year"]
lifeExp = masterList.loc[:, "Life expectancy (years)"]

expYear = int(input("Enter the year of interest: "))
print()
print(f"The overall max life expectancy is: ")
print(f"{masterList[masterList['Life expectancy (years)'] == masterList['Life expectancy (years)']. max()]}")
print(f"The overall min life expectancy is: ")
print(f"{masterList[masterList['Life expectancy (years)']== masterList['Life expectancy (years)']. min()]}")
print()
listInfo = masterList[masterList["Year"] == expYear]
meanExpLife = listInfo["Life expectancy (years)"].mean()
print(f"For the year {expYear}: ")
print(f"The average life expectancy across all countries was {float(meanExpLife):.2f}")
print(f"The max life expectancy was in : \n{listInfo[listInfo['Life expectancy (years)'] == listInfo['Life expectancy (years)']. max()]}")
print(f"The min life expectancy was in: \n{listInfo[listInfo['Life expectancy (years)']== listInfo['Life expectancy (years)']. min()]}")
print("This Informatios was Saved in txt file")
infoCard = open("InfoCard.txt","w")
infoCard.write(f"For the year {expYear}: \n")
infoCard.write(f"The average life expectancy across all countries was {float(meanExpLife):.2f}\n")
infoCard.write(f"The max life expectancy was in : \n{listInfo[listInfo['Life expectancy (years)'] == listInfo['Life expectancy (years)']. max()]}\n")
infoCard.write(f"The min life expectancy was in: \n{listInfo[listInfo['Life expectancy (years)']== listInfo['Life expectancy (years)']. min()]}")