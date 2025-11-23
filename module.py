import json
import os
import random

#Operations on the json file
def add_to_json(type, item):
    try:
        with open("database.json", "r") as file:
            if os.path.getsize("database.json") == 0:
                data = { "books": [], "users": [], "system": []}
            else:
                data = json.load(file)

            data[type.lower()].append(item)
            
            
        with open("database.json", "w") as file:
            json.dump(data, file)
            
    except FileNotFoundError:
        print("database.json not found")
        
def remove_from_json(type, name):
    try:
        with open("database.json", "r") as file:
            data = json.load(file)
            
            for item in data[type.lower()]:
               if item[list(item)[0]] == name:
                   data[type.lower()].remove(item)
            
        with open("database.json", "w") as file:
            json.dump(data, file)
            
    except FileNotFoundError:
        print("database.json not found")
        
def read_from_json(type):
    with open("database.json", "r") as file:
        data = json.load(file)[type.lower()]
        return data


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
    def __init__(self):
        self.books = read_from_json("books")
        self.users = read_from_json("users")
        
    def add_a_book(self):
        title = input("What is the name of this book?: ")
        author = input("Who is the author of this book?: ")
        isbn = input("What is the ISBN of this book?: ")

        book = Book(title, author, isbn, True)
        data = book.to_json()
        add_to_json("books", data)
        print("Book added successfully!")
        
    def remove_a_book(self):
        title = input("What is the name of the book you want to delete?: ")
        remove_from_json("books", title)
        print("Book removed successfully!")
        
    def list_books(self):
        print("Here are all the books in your library")
        data = read_from_json("books")
        for i,item in enumerate(data):
            print(f"{i+1}. {item}")
        return data

    def borrow_book(self, user_id, book_id):
        pass
    def return_book(self, user_id, book_id):
        pass