from book import Book

class Manager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.catalog = {}
            cls._instance.members = {}
            cls._instance.MAX_BOOKS_PER_MEMBER = 5
            cls._instance.LOAN_DURATION_DAYS = 14
        return cls._instance
    
    # def __init__(self,max,loan):
    #     if self._instance != None:
    #         raise Exception("Singleton class can be instanciate only once")
    #     else:
    #         self.catalog = {}
    #         self.members = {}
    #         self.MAX_BOOKS_PER_MEMBER = max
    #         self.LOAN_DURATION_DAYS = loan
    #         Manager._instance = self
    
    @staticmethod
    def get_instance():
        if Manager._instance is None:
            #default
            Manager()
        return Manager._instance
    
    def add_book(self,book):
        self.catalog[book.isbn] = book
        
    def remove_book(self,isbn):
        self.catalog.pop(isbn,None)
    
    def get_book(self,isbn):
        return self.catalog.get(isbn)
        
    def register_member(self,member):
        self.members[member.id] = member
        
    def unregister_member(self,id):
        self.members.pop(id,None)
        
    def get_member(self,id):
        return self.members.get(id)
    
    def borrow_book(self, id, isbn):
        member = self.get_member(id)
        book = self.get_book(isbn)
        
        if member and book and book.available:
            if len(member.borrowed_books) < self.MAX_BOOKS_PER_MEMBER:
                member.borrow_book(book)
                book.available = False
                print(f"Book borrowed: {book.name} by {member.name}")
        else:
            print(f"Book is not available or member is not found")
        
    def return_book(self, id, isbn):
        member = self.get_member(id)
        book = self.get_book(isbn)
        
        if member and book:
            member.return_book(book)
            book.available = True
            print(f"Book returned: {book.name} by {member.name}")
        else:
            print("Book or member not found")
    
    def search_books(self, keyword):
        matching_books = [book for book in self.catalog.values() if keyword in book.name or keyword in book.author]
        return matching_books
            