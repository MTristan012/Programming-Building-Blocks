"""
By: Tristan Perea
11 Prove Assignment Milestone
"""

maxYear = -1
maxExpLife = -1
maxCountry = ""

minYear = 9999
minExpLife = 9999
minCountry = ""

newMaxExpLife = -1
newMaxCountry = ""

newMinExpLife = 9999
newMinCountry = ""

nMaxExpLife = -1
nMaxYear = -1

nMinExpLife = 9999
nMinYear = 9999

sumAll = 0
counter = 0

nSumAll = 0
nCounter = 0

expYear = int(input("Enter the year of interest: "))
expCountry = input("Enter the Country of interest: ").title()

with open("life-expectancy.csv") as masterList:
    next(masterList)
    for section in masterList:
        cleanMasterList = section.strip()
        lineMasterList = cleanMasterList.split(",")
        completList = lineMasterList
        fullList = lineMasterList
        country = lineMasterList[0]
        year = int(lineMasterList[2])
        yearExp = year
        lifeExp = float(lineMasterList[3])
        if lifeExp > maxExpLife:
            maxYear = year
            maxExpLife = lifeExp
            maxCountry = country
        if lifeExp < minExpLife:
            minYear = year
            minExpLife = lifeExp
            minCountry = country
        fcountry = completList[0]
        fYear = float(completList[2])
        fExpLife = float(completList[3])
        if fYear == expYear:
            sumAll += fExpLife
            counter += 1
            if fExpLife > newMaxExpLife:
                newMaxExpLife = fExpLife
                newMaxCountry = country
            if fExpLife < newMinExpLife:
                newMinExpLife = fExpLife
                newMinCountry = fcountry
        nCountry = fullList[0]
        nYear = int(fullList[2])
        nExpLife = float(fullList[3])
        if nCountry == expCountry:
            nSumAll += nExpLife
            nCounter += 1
            if nExpLife > nMaxExpLife:
                nMaxExpLife = nExpLife
                nMaxYear = nYear
            if nExpLife < nMinExpLife:
                nMinExpLife = nExpLife
                nMinYear = nYear

print()
print(
    f"The overall max life expectancy is: {maxExpLife} from {maxCountry} in {maxYear}")
print(
    f"The overall min life expectancy is: {minExpLife} from {minCountry} in {minYear}")
print()
print(f"For the year {expYear}:")
print()
mean = round(sumAll/counter,2)
print(f"The average life expectancy across all countries was {mean}")
print(
    f"The max life expectancy was in {newMaxCountry} with {newMaxExpLife}")
print(
    f"The min life expectancy was in {newMinCountry} with {newMinExpLife}")
print()
print(f"For the Entity {expCountry}:")
print()
nMean = round(nSumAll/nCounter, 2)
print(f"The average life expectancy for this country was {nMean}")
print(
    f"The max life expectancy was in {nMaxYear} with {nMaxExpLife}")
print(
    f"The min life expectancy was in {nMinYear} with {nMinExpLife}")
print()
print("This information was saved in a txt file")
infoCard = open("InfoCard.txt", "w")
infoCard.write(f"For the year {expYear}: \n")
infoCard.write(
    f"The average life expectancy across all countries was {float(sumAll/counter):.2f}\n")
infoCard.write(
    f"The max life expectancy was in {newMaxCountry} with {newMaxExpLife}\n")
infoCard.write(
    f"The min life expectancy was in {newMinCountry} with {newMinExpLife}\n")
infoCard.write(f"For the Entity {expCountry}: \n")
infoCard.write(
    f"The average life expectancy across for this Country was {float(nSumAll/nCounter):.2f}\n")
infoCard.write(
    f"The max life expectancy was in {nMaxYear} with {nMaxExpLife}\n")
infoCard.write(
    f"The min life expectancy was in {nMinYear} with {nMinExpLife}\n")
