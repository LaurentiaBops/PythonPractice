from book import Book
from users import User


class Library:
    def __init__(self, name) -> None:
        self.name = name #Name of the library'
        self.books: list[Book] = []
        self.users: User = []  




