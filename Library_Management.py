"""Design a library system with late fine calculation.
Requirements:
Class Book → title, author, book_id
Class Member → name, member_id
Class Library containing list of Books & Members
Implement:
Issue a book
Return a book
Calculate fine if returned late
Fine rule:
₹5 per extra day after 7 days
Track which member has borrowed which book."""
from datetime import datetime
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = False
        self.issued_to = None
        self.issue_date = None

    def __str__(self):
        if self.is_issued:
            return f"[{self.book_id}] {self.title} by {self.author} - (Issued to {self.issued_to.name})"
        return f"[{self.book_id}] {self.title} by {self.author} - (Available)"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"[{self.member_id}] {self.name}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, book_id):
        # check duplicate
        if self.find_book(book_id):
            print(" Book ID already exists!")
            return
        self.books.append(Book(title, author, book_id))
        print(" Book Added Successfully!")

    def add_member(self, name, member_id):
        # check duplicate
        if self.find_member(member_id):
            print(" Member ID already exists!")
            return
        self.members.append(Member(name, member_id))
        print(" Member Added Successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print(" Book not found!")
            return
        if not member:
            print(" Member not found!")
            return
        if book.is_issued:
            print(" Book already issued!")
            return

        book.is_issued = True
        book.issued_to = member
        book.issue_date = datetime.today()

        print(f" Book '{book.title}' issued to {member.name} on {book.issue_date.date()}")

    def calculate_fine(self, issue_date, return_date):
        days = (return_date - issue_date).days

        if days <= 7:
            return 0

        extra_days = days - 7
        fine = extra_days * 5
        return fine

    def return_book(self, book_id):
        book = self.find_book(book_id)

        if not book:
            print(" Book not found!")
            return
        if not book.is_issued:
            print(" Book is not issued!")
            return

        return_date = datetime.today()
        fine = self.calculate_fine(book.issue_date, return_date)

        print(f" Book '{book.title}' returned by {book.issued_to.name} on {return_date.date()}")

        if fine > 0:
            print(f" Late Fine = ₹{fine}")
        else:
            print(" No Fine (Returned within 7 days)")
        
        # Reset book info
        book.is_issued = False
        book.issued_to = None
        book.issue_date = None

    def show_books(self):
        if not self.books:
            print(" No books in library!")
            return

        print("\n All Books:")
        for book in self.books:
            print(book)

    def show_members(self):
        if not self.members:
            print(" No members in library!")
            return

        print("\n All Members:")
        for member in self.members:
            print(member)

    def show_borrowed_books(self):
        found = False
        print("\n Borrowed Books:")
        for book in self.books:
            if book.is_issued:
                found = True
                print(f"{book} | Issued On: {book.issue_date.date()}")
        if not found:
            print(" No books are currently issued.")

# MAIN MENU PROGRAM
lib = Library()
while True:
    print("\n========== LIBRARY MENU ==========")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show All Members")
    print("7. Show Borrowed Books")
    print("8. Exit")

    choice = input("Enter your choice(1-8): ")
    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        lib.add_book(title, author, book_id)

    elif choice == "2":
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Member Name: ")
        lib.add_member(name, member_id)

    elif choice == "3":
        book_id = int(input("Enter Book ID to Issue: "))
        member_id = int(input("Enter Member ID: "))
        lib.issue_book(book_id, member_id)

    elif choice == "4":
        book_id = int(input("Enter Book ID to Return: "))
        lib.return_book(book_id)

    elif choice == "5":
        lib.show_books()

    elif choice == "6":
        lib.show_members()

    elif choice == "7":
        lib.show_borrowed_books()

    elif choice == "8":
        print(" Exiting Library System... Bye ")
        break

    else:
        print(" Invalid Choice! please enter from 1 to 8 only.")