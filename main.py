import json
import os
import module
import random


# ##T0D0
#Move functions to module.py as part of the classes

defaultData = { "books": [], "users": [], "system": []}

#Operations on the json file
def add_to_json(type, item):
    try:
        with open("database.json", "r") as file:
            if os.path.getsize("database.json") == 0:
                data = defaultData
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


#Librarians Options
def librarian_roles():
    print("Here are your options:\n1. Add a book\n2. Remove a book\n3. Check all the books\n4. Permit book borrowing\n5. Permit book returning")
    choice = input("What would you like to do first?: ")
    
    if choice == "1":
        add_a_book()
    elif choice == "2":
        remove_a_book()
    elif choice == "3":
        check_all_books()
    
#Adding a book to the system
def add_a_book():
    title = input("What is the name of this book?: ")
    author = input("Who is the author of this book?: ")
    isbn = input("What is the ISBN of this book?: ")
    book = module.Book(title, author, isbn, True)
    
    data = book.to_json()
    add_to_json("books", data)
    print("Book successfully added to the system!")
    
#Removing a book from the system
def remove_a_book():
    title = input("What is the name of the book you want to delete?: ")
    remove_from_json("books", title)
    print("Book printed successfully!")
    
def check_all_books():
    print("Here are all the books in your library")
    data = read_from_json("books")
    for i,item in enumerate(data):
        print(f"{i+1}. {item}")
    return data
    
def authenticate_user():
    has_account = input("Are you already a user in this library (y/n)?: ").lower()
    if has_account == "y":
        name = input("What is your account name?: ").lower()
        data = read_from_json("users")
        for item in data:
            if item["name"] == name:
                user1 = item
            else:
                print("Usernot found!")
                print("You are not part of this library.")
    sign_up()
    user_roles()
                
def sign_up():
    choice = input("Would you like to join this library (y/n)?: ").lower()
    if choice == "y":
        add_user()
    else:
        print("Sad to see you go")
    
def add_user():
    name = input("What is your name(username)?: ") 
    user_id = random.randint(1000, 9999)
    user = module.User(name, user_id, []).to_json()
    
    add_to_json("users", user)
    print("User added successfully!")
        
#Users Options
def user_roles():
    print("Here are your options:\n1. Borrow a book\n2. Return a book")
    choice = input("What would you like to do first?: ")
    
    if choice == "1":
        borrow_a_book()
    elif choice == "2":
        return_a_book()
        
def borrow_a_book():
    books = check_all_books()
    book_choice = int(input("Which book would you like to borrow?: "))
    book = books[book_choice-1]  
        

def return_a_book():
    pass
    

###############################################################Beginning of program
# print("Welcome to your library system!")
# role = input("Are you a librarian (1) or a user(2)?: ")

# if role == "1":
#     librarian_roles()
# elif role == "2":
#     authenticate_user()
