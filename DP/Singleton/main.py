# A Singleton pattern in python is a design pattern that allows you to 
# create just one instance of a class, throughout the lifetime of a program.

class SingleTonClass:
    __instance = None
    
    @staticmethod
    def get_instance():
        if SingleTonClass.__instance == None:
            SingleTonClass("Default Name", 0)
        return SingleTonClass.__instance
    
    def __init__(self, name, age):
        if SingleTonClass.__instance != None:
            raise Exception("Singleton class can be instanciate only once")
        else:
            self.name = name
            self.age = age
            SingleTonClass.__instance = self
        
    @staticmethod
    def print_data():
        print(f"Name is {SingleTonClass.__instance.name}")
        
s1 = SingleTonClass("bhavya", 25)
s1.print_data()
s2 = s1.get_instance()
print(s2.name)