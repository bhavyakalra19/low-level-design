from book import Book
from member import Member
from manager import Manager

class LMS:
    @staticmethod
    def run():
        # lm = Manager(5,14)
        # l1 = Manager(5,100)
        # library_manager = lm.get_instance()
        
        library_manager = Manager.get_instance()
        
        library_manager.add_book(Book("isbn1", "Book 1", "Author 1", 2020))
        library_manager.add_book(Book("isbn2", "Book 2", "Author 2", 2019))
        library_manager.add_book(Book("isbn3", "Book 3", "Author 3", 2021))
        
        library_manager.register_member(Member(1, "Bhavya Kalra", "bkbkbhavyakalra@gmail.com"))
        library_manager.register_member(Member(2, 'Chiransh Kalra', "chiranshkalra@gmail.com"))
        
        library_manager.borrow_book(1,"isbn1")
        library_manager.borrow_book(2,"isbn2")
        
        library_manager.return_book(1,"isbn1")
        
        search_results = library_manager.search_books("Book")
        print("search_results: ")
        for book in search_results:
            print(f"{book.name} by {book.author}")
        
if __name__ == "__main__":
    LMS.run()