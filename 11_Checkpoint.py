"""
By: Tristan Perea
11 Checkpoint
"""

with open("books.txt") as booksList:
    for book in booksList:
        print(book.strip())

