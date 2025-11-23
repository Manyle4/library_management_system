class Book:
    def __init__(self, title, author, isbn, isAvailable):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = isAvailable
        
    def mark_borrowed(self):
        pass
    def mark_returned(self):
        pass
    def to_json(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "availability": self.isAvailable}
    
class User:
    def __init__(self, name, user_id, borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books
        
    def borrow_book(self,book):
        pass
    def return_book(self,book):
        pass
    def to_json(self):
        return {"name": self.name, "user_id": self.user_id, "borrowed_books": self.borrowed_books}
    
class Library:
    def __init__(self, books, users):
        self.books = books
        self.users = users
        
    def add_books(self):
        pass
    def remove_books(self):
        pass
    def list_books(self):
        pass
    def borrow_book(self, user_id, book_id):
        pass
    def return_book(self, user_id, book_id):
        pass
    def save_to_file(self):
        pass
    def load_from_file(self):
        pass