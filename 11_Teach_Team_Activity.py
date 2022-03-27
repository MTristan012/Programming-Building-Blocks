"""
By: Tristan Perea
10 Team Activity
"""

with open("hr_system.txt") as masterList:
    for dataLine in masterList:
        clean_line = dataLine.strip()
        parts = clean_line.split(" ")
        name = parts[0]
        idNumber = parts[1]
        title = parts[2]
        salary = float(parts[3])
        payAmount = salary / 24
        if title.lower() == "engineer":
            payAmount += 1000
        print(f"{name} (ID: {idNumber}), {title} - ${payAmount:.2f}")
