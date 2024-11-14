# The Liskov Substitution Principle is a fundamental principle in oops
# that states that objects of a superclass should be able to replaced 
# with objects of a subclass without affecting the correctness of the program


# In below example, we have a base class shape with a method area() which 
# calculates the area of a shape. There are two derived classes, Rectangle
# and Square which inherit from the shape class and implement their own 
# version of calculating area but it always give area in evry situation

class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.height * self.width
    
class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
def print_area(shape):
    print(f"area is {shape.area()}")
    
r1 = Rectangle(2,3)
print_area(r1)

s1 = Square(4)
print_area(s1)

