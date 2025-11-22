import json
import module


# ##T0D0
# Fix the add to json function to work on multiple json objects
# Try the read from json


#Librarians Options
def librarian_roles():
    print("Here are your options:\n1. Add a book\n2. Remove a book\n3. Check all the books\n4. Permit book borrowing\n5. Permit book returning")
    choice = input("What would you like to do first?: ")
    
    if choice == "1":
        add_a_book()
    elif choice == "2":
        remove_a_book()
    
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
    
#Users Options
def user_roles():
    print("Here are your options:\n1. Borrow a book\n2. Return a book")
    choice = input("What would you like to do first?: ")
    

#Operations on the json file
def add_to_json(type, item):
    try:
        with open("database.json", "r") as file:
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
        print(data)


###############################################################Beginning of program
print("Welcome to your library system!")
# role = input("Are you a librarian (1) or a user(2)?: ")

# if role == "1":
#     librarian_roles()
# elif role == "2":
#     user_roles()

# read_from_json("books")
add_a_book()