# library_management_system
A terminal based library management system to practice OOP and creating classes using python. This is a simple library management system to help me practice programming in python using the Linux Ubuntu OS

# Structure
This program uses 3 main classes: Book, User and Library

## Book
Attributes:
title
author
isbn
available (True/False)
Methods:
mark_borrowed()
mark_returned()

## User
Attributes:
name
user_id
borrowed_books (list)
Methods:
borrow_book(book)
return_book(book)

## Library
Attributes:
books (list of Book objects)
users (list of User objects)
Methods:
add_book()
remove_book()
list_books()
borrow_book(user_id, book_id)
return_book(user_id, book_id)
save_to_file()
load_from_file()