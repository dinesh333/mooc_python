# Please write a class named Book with the attributes name, author, genre and year, 
# along with a constructor which assigns initial values to these attributes.

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year