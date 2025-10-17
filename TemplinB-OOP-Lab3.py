class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""
    def add_book(self):
        self.book_id = input("Enter Book ID: ")
        self.book_title = input("Enter Book Title: ")
        self.author_id = input("Enter Author ID: ")
        self.publisher = input("Enter Publisher: ")
        self.year_of_publication = input("Enter Year of Publication: ")
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Book Title:", self.book_title)
        print("Author ID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year of Publication:", self.year_of_publication)

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.author_phone = ""
        self.email_id_author = ""
    def add_author(self):
        self.author_id = input("Enter Author ID: ")
        self.author_name = input("Enter Author Name: ")
        self.affiliation = input("Enter Affiliation: ")
        self.country = input("Enter Country: ")
        self.author_phone = input("Enter Phone: ")
        self.email_id_author = input("Enter Email: ")
    def display_author(self):
        print("Author ID:", self.author_id)
        print("Author Name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.author_phone)
        print("Email:", self.email_id_author)

class User:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email_id_user = ""
        self.books_borrowed = []
    def add_user(self):
        self.user_id = input("Enter User ID: ")
        self.name = input("Enter User Name: ")
        self.password = input("Enter User Password: ")
        self.address = input("Enter User Address: ")
        self.phone = input("Enter User Phone: ")
        self.email_id_user = input("Enter Email: ")
    def display_user(self):
        print("User ID:", self.user_id)
        print("User Name:", self.name)
        print("User Password:", self.password)
        print("User Address:", self.address)
        print("User Phone:", self.phone)
        print("User Email:", self.email_id_user)
    def add_borrowed_books(self, b):
        self.books_borrowed.append(b)
    def display_borrowed_books(self):
        for book in self.books_borrowed:
            print("Book Borrowed:", book.book_title)

while True:
    print("1. Initialize Classes")
    print("2. Add Book")
    print("3. Display Book")
    print("4. Add Author")
    print("5. Display Author")
    print("6. Add User")
    print("7. Display User")
    print("8. Add Borrowed Book")
    print("9. Display Borrowed Book")
    print("10. Exit Program")
    option = input("Enter Option: ")

    if option == "1":
        b1 = Book()
        b2 = Book()
        b3 = Book()
        a1 = Author()
        u1 = User()

    if option == "2":
        b1.add_book()
        b2.add_book()
        b3.add_book()

    elif option == "3":
        b1.display_book()
        b2.display_book()
        b3.display_book()


    elif option == "4":
        a1.add_author()

    elif option == "5":
        a1.display_author()

    elif option == "6":
        u1.add_user()

    elif option == "7":
        u1.display_user()

    elif option == "8":

        while True:
            print("1.", b1.book_title)
            print("2.", b2.book_title)
            print("3.", b3.book_title)
            print("4. Exit")
            option_book = input("Enter Which Book to Borrow: ")

            if option_book == "1":
                u1.add_borrowed_books(b1)

            elif option_book == "2":
                u1.add_borrowed_books(b2)

            elif option_book == "3":
                u1.add_borrowed_books(b3)

            elif option_book == "4":
                break

    elif option == "9":
        u1.display_borrowed_books()

    elif option == "10":
        break


