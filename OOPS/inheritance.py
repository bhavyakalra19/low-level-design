class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    

class Student(Person):
    def __init__(self,fname,lname,age):
        #super method is used to revoke the parents methods
        super().__init__(fname,lname)
        self.age = age
        
        
s1 = Student("Bhavya", "Kalra", 25)

print(f"My name is {s1.fname} {s1.lname} and age is {s1.age}")