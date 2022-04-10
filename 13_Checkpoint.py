"""
By: Tristan Perea
13 Checkpoint
"""

def theMessage(message):
    print(message)
    titMessage = message.title()
    print(titMessage)
    lowMessage = message.lower()
    print(lowMessage)
    upMessage = message.upper()
    print(upMessage)

message = input("What is your message? ")
theMessage(message)
