class Machine:
    #All method need to be implemented as a core part of Machine
    def print(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError
    
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass

class OldFashionPrinter(Machine):
    def print(self, document):
        pass
    #In old fashioned printer we can not do scan and fax if someone sees fax method in 
    #oldfashion it will show error of not implemented