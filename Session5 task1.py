class Book:
 def __init__(self, title, author, isbn, available=True):
  self.title = title
  self.author = author
  self.isbn = isbn
  self.available = available
 def display(self):
  print(f"{self.title}, {self.author}, {self.isbn}, {'Available' if self.available else 'Not Available'}")
class Member:
 def __init__(self, name, membership_id):
  self.name = name
  self.membership_id = membership_id
  self.borrowed_books = []
 def borrow(self, book):
  if book.available:
   self.borrowed_books.append(book)
   book.available = False
   print(f"{self.name} borrowed {book.title}")
  else:
   print(f"{book.title} not available")
 def return_book(self, book):
  if book in self.borrowed_books:
   self.borrowed_books.remove(book)
   book.available = True
   print(f"{self.name} returned {book.title}")
  else:
   print(f"{self.name} didn't borrow {book.title}")
b = Book("Python", "omar", "444")
m = Member("karas", "44")
b.display()
m.borrow(b)
b.display()
m.return_book(b)
b.display()