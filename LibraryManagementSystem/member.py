class Member:
    def __init__(self, id, name, contact):
        self._id = id
        self._name = name
        self._contact = contact
        self._borrowed_books = []
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact
    
    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    def borrow_book(self,book):
        self._borrowed_books.append(book)
    
    def return_book(self,book):
        self._borrowed_books.remove(book)