class Book:
    def __init__(self, isbn, name, author, publish_year):
        self._isbn = isbn
        self._name = name
        self._author = author
        self._publish_year = publish_year
        self._available = True
        
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author
    
    @property
    def publish_year(self):
        return self._publish_year
    
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, avail):
        self._available = avail
        

