"""
By: Tristan Perea
03 checkpoint
"""
age = int(input("How old are you?: "))
age = age + 1
print("On your next birthday, you will be " + str(age))
print()
eggs = int(input("How many egg cartons do you have? "))
eggs = eggs * 12
print("You have " + str(eggs) + " eggs")
print()
cookies =int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
cookiesp = cookies/people
print("Each person may have " + str(cookiesp) +" cookies")