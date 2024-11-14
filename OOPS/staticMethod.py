# A static method does not receive an implicit first argument. 
# A static method is also a method that is bound to the class 
# and not the object of the class. This method can’t access or 
# modify the class state. It is present in a class because it
# makes sense for the method to be present in class.

class Person:
    def __init__(self,age):
        self.age = age
    
    @staticmethod
    def getMaxAge(x,y):
        return max(x,y)

p1 = Person(25)

print(p1.getMaxAge(25,27))