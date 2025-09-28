

class Book:
    def __init__(self,title):
        self.title=title
        self.is_borrowed=False

class Library:
    def __init__(self):
        self.books=[]

    def add_books(self,titles):
        for t in titles:
            self.books.append(Book(t))  # self.books=Book("title") garya jasto ho yo
    def borrow_books(self,title):
        for book in self.books:
            if book.title==title and book.is_borrowed==False:
                self.is_borrowed=True
                print(f"{book.title} is borrowed")
            return
        print(f"{book.title} is not available")
    

    def display_books(self):
        print("Library collection:")
        for book in self.books:
            status="Available" if not book.is_borrowed else "Borrowed"
            print(f"{book.title}->{status}")

o1=Library()
o1.add_books(["Real Analysis",'matrix theory','modern algebra'])
# o1.display_books()

o1.borrow_books("Real Analysis")
o1.display_books()


