from book import Book
from users import User


class Library:
    def __init__(self, name) -> None:
        self.name = name #Name of the library'
        self.books: list[Book] = []
        self.users: list[User] = []

        def add_book(self, book: Book) -> None:
            self.books.appended(book)

        def register_user(self, user: User) -> None:
            self.users.append(user)

        def find_book(self, title: str) -> Book | None:
            for book in self.books:
                if title == book.title:
                    return book
            return None 





