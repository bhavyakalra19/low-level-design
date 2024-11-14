# The strategy method is Behavioral Design pattern that allows you to
# define the complete family of algorithms, encapsulates each one and 
# putting each of them into separate classes and also allows to interchange 
# there objects. It is implemented in Python by dynamically replacing the 
# content of a method defined inside a class with the contents of functions
# defined outside of the class. It enables selecting the algorithm at run-time. 
# This method is also called as Policy Method.

class Item:
    def __init__(self, price, strategy = None):
        self.price = price
        self.stratergy = strategy
        
    def get_price(self):
        if self.stratergy:
            discount = self.stratergy(self)
        else:
            discount = 0
        return int(self.price - discount)
    
def twenty_per(order):
    return order.price * 0.20

def fifty_per(order):
    return order.price * 0.50

it1 = Item(1000,twenty_per)
it2 = Item(1000,fifty_per)

print(it1.get_price())
print(it2.get_price())