class Rectangle:
    
    def __init__(self,height,width):
        self._height = height
        self._width = width
        
    @property
    def area(self):
        return self._height * self._width
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width = value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height = value
    
    
class Square(Rectangle):
    def __init__(self,size):
        super().__init__(self,size,size)
    
    @Rectangle.width.setter
    def width(self,value):
        self._width = self._height = value
        
    @Rectangle.height.setter
    def height(self,value):
        self._width = self._height = value
        

def use_it(rc):
    w = rc.width
    rc.height = 10
    
    expected = int(w*10)
    print(f"Expected {expected}, got {rc.area}")
    
r1 = Rectangle(2,3)
use_it(r1)

r2 = Square(4)
use_it(r2)