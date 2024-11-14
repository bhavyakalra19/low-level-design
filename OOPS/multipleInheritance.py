class Class1:
    def print_string(self):
        print("In class1")
        
class Class2(Class1):
    def print_string(self):
        print("In class2")
        
class Class3:
    def print_string(self):
        print("In Class3")
        
class ChildClass(Class2,Class3):
    pass

p1 = ChildClass()

print(p1.print_string())