import json

#Librarians Options
def librarian_roles():
    print("Here are your options:\n1. Add a book\n2. Remove a book\n3. Check all the books\n4. Permit book borrowing\n5. Permit book returning")
    choice = input("What would you like to do first?: ")
    
#Users Options
def user_roles():
    print("Here are your options:\n1. Borrow a book\n2. Return a book")
    choice = input("What would you like to do first?: ")

print("Welcome to your library system!")

role = input("Are you a librarian (1) or a user(2)?: ")

if role == "1":
    librarian_roles()
elif role == "2":
    user_roles()
