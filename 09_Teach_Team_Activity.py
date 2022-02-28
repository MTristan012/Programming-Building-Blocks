"""
By: Tristan Perea
09 Team Activity
"""
from audioop import avg

from numpy import average


listNum = []
newNum = ""

print("Enter a list of numbers, type 0 when finished.")

while newNum != 0:
    newNum = int(input("Enter number: "))
    listNum.append(newNum)

listNum.pop()

listSum = sum(listNum)
print("The sum is: " + str(listSum))

listProm = average(listNum)
print("The average is: " + str(listProm))

print("The largest number is: " + str(max(listNum)))

smallPositive = filter(lambda x: x >= 0, listNum)
print("The smallest positive number is: " + str(min(smallPositive)))

sortedList = sorted(listNum)
print("The sorted list is: ")
for element in sortedList:
    print(element)
