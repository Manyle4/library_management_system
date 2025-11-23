import json
import os
import module
import random

# ##T0D0
#Allow a user to borrow a book and return a book

#Librarians Options
def librarian_roles():
    print("Here are your options:\n1. Add a book\n2. Remove a book\n3. Check all the books\n4. Permit book borrowing\n5. Permit book returning")
    choice = input("What would you like to do first?: ")
    
    if choice == "1":
        library.add_a_book()
    elif choice == "2":
        library.remove_a_book()
    elif choice == "3":
        library.list_books()
    
    
# #Users Options
def user_roles():
    print("Here are your options:\n1. Borrow a book\n2. Return a book")
    choice = input("What would you like to do first?: ")
    
    # if choice == "1":
    #     borrow_a_book()
    # elif choice == "2":
    #     return_a_book()
        
# def borrow_a_book():
#     books = check_all_books()
#     book_choice = int(input("Which book would you like to borrow?: "))
#     book = books[book_choice-1]  
        

# def return_a_book():
#     pass

def sign_up():
    choice = input("Would you like to join this library (y/n)?: ").lower()
    if choice == "y":
        name = input("What is your name(username)?: ").lower() 
        user_id = random.randint(1000, 9999)
        user = module.User(name, user_id, []).to_json()
    
        module.add_to_json("users", user)
        print("User added successfully!")
        user_roles()
    else:
        print("Sad to see you go")


def authenticate_user():
    has_account = input("Are you already a user in this library (y/n)?: ").lower()
    if has_account == "y":
        name = input("What is your account name?: ").lower()
        data = module.read_from_json("users")
        for item in data:
            if item["name"] == name:
                print(f"Welcome to the library {item["name"].capitalize()} !")
                user_roles()
            else:
                print("User not found!")
                print("You are not a user of this library")
                sign_up()
        
###############################################################Beginning of program
print("Welcome to your library system!")
library = module.Library()
role = input("Are you a librarian (1) or a user(2)?: ")

if role == "1":
    librarian_roles()
    pass
elif role == "2":
    authenticate_user()
