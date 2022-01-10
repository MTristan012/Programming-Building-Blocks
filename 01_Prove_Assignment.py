"""
File: 01_Prove Assignment
Author: MTristan Perea

"""

Name = input("Hello World!! I'm Tristan & this is my 2nd code!, Tell me What is your name?: ")
print("Hello " + Name + " you are welcome!!!")
print("You are my Instructor?")
Answer = int(input("If that is correct, put 1 here, if not and you are a partner put 0: "))
if Answer==1:
    print("Nice to meet you Mr " + Name)
elif Answer==0:
    print("Sorry! Nice to meet you partner " + Name)
else:
    print("Sorry, your answer is not correct ")
