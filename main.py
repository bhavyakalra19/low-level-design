#member - name, book array, add_book, remove_book, borrowed_books, id, get_id, get_name, contact
class Member:
    def __init__(self, id, name, contact):
        self._id = id
        self._name = name
        self._contact = contact
        self._borrowed_books = []
        
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def contact(self):
        return self._contact
    
    @property
    def borrowed_books(self):
        return self._borrowed_books

    def add_book(self,book):
        self._borrowed_books.append(book)
        
    def remove_book(self,book):
        self._borrowed_books.remove(book)

#book - isbn, name, author, available
class Book:
    def __init__(self, isbn, name, author):
        self._isbn = isbn
        self._name = name
        self._author = author
        self._available = True
        
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def name(self):
        return self._name
    
    @property
    def author(self):
        return self._name
    
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, avail):
        self._available = avail
        

#manager - create instance, register_member, unregister_member, add_book, remove_book, get_book, get_member, borrow_book, return book, search book
class Manager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.catalog = {}
            cls._instance.members = {}
            cls._instance.MAX_BOOKS = 5
        return cls._instance
    
    @staticmethod
    def get_instance():
        if Manager._instance is None:
            Manager()
        return Manager._instance

    def register_member(self,member):
        self.members[member.id] = member
    
    def unregister_member(self,member):
        self.members.pop(member.id)
        
    def get_member(self,id):
        return self.members.get(id)
    
    def add_book(self,book):
        self.catalog[book.isbn] = book
        
    def remove_book(self,isbn):
        self.catalog.pop(isbn)
        
    def get_book(self,isbn):
        return self.catalog.get(isbn)
    
    def borrow_book(self,id,isbn):
        member = self.get_member(id)
        book = self.get_book(isbn)
        
        if member and book and book.available:
            if len(member.borrowed_books) < self.MAX_BOOKS:
                member.add_book(book)
                book.available = False
                print(f"{member.name} borrowed book {book.name}")
            else:
                print(f"{member.name} already has max limit of books i.e. {self.MAX_BOOKS}")
        else:
            print(f"Either book or member is not available")
    
    def return_book(self,id,isbn):
        member = self.get_member(id)
        book = self.get_book(isbn)
        
        if member and book:
            book.available = True
            member.remove_book(book)
            print(f"{member.name} returned book: {book.name}")
        else:
            print(f"Either book or member is not available")
            
    def search_book(self, word):
        books = self.catalog.values()
        total_books = [book for book in books if word in book.name or word in book.author]
        return total_books
#LMS

class LMS:
    @staticmethod
    def run():
        library_manager = Manager.get_instance()
        
        library_manager.add_book(Book("isbn1", "Book 1", "Author 1"))
        library_manager.add_book(Book("isbn2", "Book 2", "Author 2"))
        library_manager.add_book(Book("isbn3", "Book 3", "Author 3"))
        
        library_manager.register_member(Member(1, "Bhavya Kalra", "bkbkbhavyakalra@gmail.com"))
        library_manager.register_member(Member(2, 'Chiransh Kalra', "chiranshkalra@gmail.com"))
        
        library_manager.borrow_book(1,"isbn1")
        library_manager.borrow_book(2,"isbn2")
        
        library_manager.borrow_book(2,"isbn2")
        
        search_results = library_manager.search_book("Book")
        print("search_results: ")
        for book in search_results:
            print(f"{book.name} by {book.author}")
        
if __name__ == "__main__":
    LMS.run()