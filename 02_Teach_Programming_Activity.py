"""
File: 02 Teach: Programming Activity
Author: MTristan Perea
"""
#libraries
from datetime import datetime

#Global Variables
now = datetime.now() 
now = now.month #in this part take from datetime only the month

#In this If I convert the numeric month in a string month
if now == 1:
    now = "January"
elif now == 2:
    now = "February"
elif now == 3:
    now = "March"
elif now == 4:
    now = "April"
elif now == 5:
    now = "May"
elif now == 6:
    now = "Jun"
elif now == 7:
    now = "Jul"
elif now == 8:
    now = "August"
elif now == 9:
    now = "September"
elif now == 10:
    now = "October"
elif now == 11:
    now = "November"
elif now == 12:
    now = "December"
else:
    now = "The End of Times"

#Here start the essencial code
print("Please enter the following information: ")

print()
name = input("First Name: ") # In his variable save the name
lastName = input("Last Name: ")  # In his variable save the last name
email = input("Email Address: ")  # In his variable save the email address
phonenumber = input("Phone Number: ")  # In his variable save the phone number
job = input("Job Title: ")  # In his variable save the job title
idNumber = input("ID Nummber: ")  # In his variable save the nID number
#Stretch Challenge
haircolor = input("Color of your Hair: ")  # In his variable save the hair color
eyescolor = input("Color of your Eyes: ")  # In his variable save the eyes color
training = input("Are you in Training?: ")  # In his variable save the answer

print() 
print("The ID Card is: ")
print("--------------------------------------------------")
print(lastName.upper() + ", " + name.capitalize()) # .upper() convert all letters in CAPS, .capitalize() convert the first letter in CAPS
print(job.title()) #.title() convert every first letter in CAPS
print("ID: " + idNumber)
print()
print(email.lower()) #.lower() convert all letters lowercase
print(phonenumber)
print()
#Stretch Challenge
print(("Hair: " + haircolor.capitalize() + "\t" + "Eyes: " + eyescolor.capitalize()).expandtabs(30))
print(("Month: "+ now + "\t" + "Trainig: " + training.capitalize()).expandtabs(30))
print("--------------------------------------------------")