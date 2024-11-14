# "Objects or entities should be open for extension but closed for modification"

# This means a class should be extendible without modifying the class itself

# The open-closed principle states that a module should be open for extension
# but not for modification, a module should be designed in such a way that it can be
# easily extended without changing its existing code

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        return self.l * self.w
    
def calculate_area(shapes):
    return sum([shape.area() for shape in shapes])

shapes = [Circle(2), Rectangle(2,4), Circle(4), Rectangle(4,8)]

print(f"Total Area: {calculate_area(shapes)}")