# To make effective use of LSP it's important to avoid certain pitfalls


# 1. Derived class shoulf not violate the contracts defined by the class.
# If a derived class modifies or ignores the req of base class it can lead to inconsistencies

class Bird:
    def fly(self):
        print("fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cant fly") #This causes inconsistencies
        
        
        
        

# 2. Tight coupling with Implementations details
# In below situation a connect method is tightly coupled with class implementation

class DatabaseConnector:
    def connect(self):
        pass

class MysqlConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to mysql database")
        
class PostgresqlConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to postgresql database")


# 3. Dont modify child class attributes for sake of base class method as it violates the Liskov Subs prin 
# If a square class is derived from Rectangle class and it set attributes h and w equal to each other after calling sqaure object
# to call area method from rectangle class. This violates the LSP