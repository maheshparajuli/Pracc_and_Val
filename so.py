class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
    
    def add_books(self, titles):
        for t in titles:
            self.books.append(Book(t))
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{title}'")
                return
        print(f"'{title}' is not available")
    
    def display_books(self):
        print("\nLibrary Collection:")
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"{book.title} -> {status}")


# Example
lib = Library()
lib.add_books(["Python Basics", "Data Science", "AI with Python"])
lib.display_books()

lib.borrow_book("Python Basics")
lib.display_books()
