# Please write a function named older_book(book1: Book, book2: Book) which takes 
# two objects of type Book as its arguments. The function should print out a message 
# with the details of whichever is the older. It should print out a different message 
# if the two books were written in the same year. Please see the examples below.

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

def older_book(book1: Book, book2: Book):
    ob = book1 if book1.year < book2.year else book2
    if book1.year == book2.year:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')
    else:
        print(f'{ob.name} is older, it was published in {ob.year}')