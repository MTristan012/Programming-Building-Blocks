"""
By: Tristan Perea
08 Team Activity
"""
import math

columnsAndRows = int(input("How many columns and rows do you want in your multiplication table? "))

limit = columnsAndRows*columnsAndRows

columnsAndRows = columnsAndRows + 1

spaceRange = int(math.log10(limit)) +1

for columns in range(1,columnsAndRows):
    for rows in range(1,columnsAndRows):
        result = columns * rows
        print(f"{result:{spaceRange}}", end=" ")
    print()
