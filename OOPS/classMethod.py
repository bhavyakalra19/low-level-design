# The classmethod() is an inbuilt function in Python, which returns a class method 
# for a given function. This means that classmethod() is a built-in Python function 
# that transforms a regular method into a class method. When a method is defined using 
# the @classmethod decorator (which internally calls classmethod()), the method is 
# bound to the class and not to an instance of the class. As a result, the method 
# receives the class (cls) as its first argument, rather than an instance (self).
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    def instanceMethod(date_string):
        year, month, day = map(int, date_string.split('-'))
        return Date(year, month, day)
    
    def getData(self):
        return self.day
    
    #dunder string method which return value when obj or class instance is printed
    def __str__(self):
        return f"String is {self.year}-{self.month}-{self.day}"
    
    
date = Date(2024,11,2)
print(f"Date is {date.year}-{date.month}-{date.day}")

dateCls = Date.from_string(f"{date.year}-{date.month}-{date.day}")


print(dateCls.day)
print(dateCls.month)
print(dateCls.year)

dateObj = Date.instanceMethod(f"{date.year}-{date.month}-{date.day}")

print(dateObj.year)
print(dateObj.getData())
print(dateObj)
print(dateCls)