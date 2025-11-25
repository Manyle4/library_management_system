# library_management_system
A terminal based library management system to practice OOP and creating classes using python. This is a simple library management system to help me practice programming in python using the Linux Ubuntu OS

# Structure
This program uses 3 main classes: Book, User and Library

### Book
#### Attributes:
1. title
2. author
3. isbn
4. available (True/False)
#### Methods:
1. mark_borrowed()
2. mark_returned()

### User
#### Attributes:
1. name
2. user_id
3. borrowed_books (list)
#### Methods:
1. borrow_book(book)
2. return_book(book)

### Library
# The librarian's code is asobiolivia_hanako_kasumichaos
#### Attributes:
1. books (list of Book objects)
2. users (list of User objects)
#### Methods:
1. add_book()
2. remove_book()
3. list_books()
4. borrow_book(user_id, book_id)
5. return_book(user_id, book_id)