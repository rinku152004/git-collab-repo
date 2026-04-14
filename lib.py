"""from datetime import datetime

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
            return f"[{self.book_id}] {self.title} by {self.author} (Issued to {self.issued_to.name})"
        else:
            return f"[{self.book_id}] {self.title} by {self.author} (Available)"


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

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

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

    def issue_book(self, book_id, member_id, issue_date=None):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            print(" Book not found")
            return

        if member is None:
            print(" Member not found")
            return

        if book.is_issued:
            print(" Book already issued")
            return

        if issue_date is None:
            issue_date = datetime.today()

        book.is_issued = True
        book.issued_to = member
        book.issue_date = issue_date

        print(f" Book '{book.title}' issued to {member.name} on {issue_date.date()}")

    def calculate_fine(self, issue_date, return_date):
        days = (return_date - issue_date).days
        if days <= 7:
            return 0
        extra_days = days - 7
        return extra_days * 5

    def return_book(self, book_id, return_date=None):
        book = self.find_book(book_id)

        if book is None:
            print(" Book not found")
            return

        if not book.is_issued:
            print(" Book is not issued")
            return

        if return_date is None:
            return_date = datetime.today()

        fine = self.calculate_fine(book.issue_date, return_date)

        print(f" Book '{book.title}' returned by {book.issued_to.name} on {return_date.date()}")

        if fine > 0:
            print(f" Late Fine = ₹{fine}")
        else:
            print(" No fine")

        # reset
        book.is_issued = False
        book.issued_to = None
        book.issue_date = None

    def show_books(self):
        print("\n Book List:")
        for book in self.books:
            print(book)

    def show_members(self):
        print("\n Member List:")
        for member in self.members:
            print(member)


#  MAIN (Run Here)
lib = Library()

# Add books
lib.add_book(Book("Harry Potter", "J.K Rowling", 101))
lib.add_book(Book("Wings of Fire", "A.P.J Abdul Kalam", 102))

# Add members
lib.add_member(Member("Rinku", 1))
lib.add_member(Member("Hetal", 2))

lib.show_books()
lib.show_members()

# Issue a book
lib.issue_book(101, 1)

# Return book after late days (Example)
issue_date = datetime(2026, 1, 1)
return_date = datetime(2026, 1, 11)  # 10 days -> fine = (10-7)*5 = 15

lib.issue_book(102, 2, issue_date)
lib.return_book(102, return_date)

lib.show_books()
"""
def sum(a,b):
    sum=a + b
    print(sum)
    return sum
    
# a=int(input("Enter value of a:"))
# b=int(input("Enter vlue of b:"))
# result=sum(a,b)
# print( f"sum is:  {result}")

name=["rinku","hetal","mital","apexa","anjali"]
city=["rajkot","ahmedabad","morbi","snagar","junagadh"]
def p_len(list):
    print(len(list))

# p_len(name)
# p_len(city)
def print_list(list):
    for item in list:
        print(item, end=" ")

# print_list(name)
# print_list(city)

def fact(n):
    # fact=1
    # for i in range(1,n+1):
    #     fact*=i
    # print(fact)
    if n==0 or n==1:
        return 1
    elif n>1:
        return n * fact(n-1)
    else:
        print("factorial is not defined for negative numbers.")

# n=5
# print(f"factorial of {n} is {fact(n)}.")

def converter(usd):
    rupee=91.61*usd
    print(usd,"USD =",rupee,"INR")
    return rupee

# usd=int(input("Enter the usd:"))
# print(converter(usd))

def odd_even(num):
    if num % 2==0:
        print("Given number is EVEN")
    else :
        print("Given number is ODD")

# int=int(input("Enter any number:"))
# print(odd_even(int))
# odd_even(int)

def show(n):
    if n==0: #base case
        return
    print(n,end=" ")
    show(n-1)
    print("end",end=" ") # print end n times after all number gets printed bcz there is left a call after each function call

# show(2)

def sum(n):
    if n==0:
        return 0
    return sum(n-1) + n
        
# n=int(input("Enter any integer:"))
# print(f"sum of 1 to {n} is {sum(n)}")

def print_list(list,index=0):
    if (index==len(list)):
        return
    print(list[index],end=" ")
    print_list(list,index+1)
# list=["mango","banana","lichi","apple"]
n=int(input("how many elements are there in list:"))
fruits=[]
for i in range(n):
    i=input(f"enter item {i+1}:")
    fruits.append(i)
print_list(fruits)

print()

# creating list using single user input
n=int(input("how many elements are there in list:"))
fruits=[]
for i in range(n):
    i=input(f"enter item {i+1}:")
    fruits.append(i)
print(fruits)

