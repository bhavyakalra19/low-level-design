#Below interfaces derived can be used specifically for particular machine we create

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_fun(self, document):
        pass
    
class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldFashionPrinter(Printer):
    def print_fun(self, document):
        print(f"Printing the documnent you have sent: {document}")
        
    
class MultiFunctionPrinter(Printer,Scanner):
    def print_fun(self, document):
        print(f"Printing the documnent you have sent: {document}")
        
    def scan(self, document):
        print(f"Scanning the documnent you have sent: {document}")