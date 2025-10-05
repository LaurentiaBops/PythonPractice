from exceptions.custom_exceptions import BookNotAvaliableError, BookNotFoundError
from models.library import Library
from models.users import User 

class LibraryService:
    def __init__(self, library: Library) -> None:
        self.library = library

    def checkout_book(self, user: User, title: str):
        book = self.library.find_book(title)
    
    if book is None:
        # Raise a book not found exception
        raise BookNotFoundError(title)
        

    if not book.is_avaliable:
        # Raise a book not avaliable exception
        raise BookNotAvaiableError(title)

    def return_book(self, user: User, title: str):
        book = self.library.find_book(title)
    
    if book is None:
        raise BookNotFoundError(title)

    if book in user.burrowed_books:
        user.return_book(book)
        book.is_avaliable = True

    book.is_avaliable = False
    user.burrow_book(book) 
    print(f"{user.name} checked out book: {book.title}")








