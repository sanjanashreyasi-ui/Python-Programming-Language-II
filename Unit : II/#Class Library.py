#Class Library
#Develop a library class that has instance variables like book_name, author, and availability status. The class should provide methods to
#check out a book, return a book, and display available books. Use the __init__ constructor to initialize book details for each object.

class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            print(self.book_name, "is checked out.")
            self.available = False
        else:
            print(self.book_name, "is not available.")

    def return_book(self):
        if not self.available:
            print(self.book_name, "is returned.")
            self.available = True
        else:
            print(self.book_name, "was already available.")

    def display(self):
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Available:", self.available)
     


# Creating books
book1 = Library("HP1", "J.K. Rowling")
book2 = Library("HP2", "J.K. Rowling")
book3 = Library("HP3", "J.K. Rowling")

# Display books
book1.display()
book2.display()
book3.display()


book1.check_out()
book1.return_book()


