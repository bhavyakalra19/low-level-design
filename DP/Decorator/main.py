# Decorator Method is a Structural Design Pattern which allows you to 
# dynamically attach new behaviors to objects without changing their 
# implementation by placing these objects inside the wrapper objects 
# that contains the behaviors. 


class Num:
    def __init__(self, num):
        self.num = num
        
    def get_num(self):
        return self.num

class AddTwo(Num):
    def __init__(self,wrapper):
        self.wrapper = wrapper
    
    def get_num(self):
        return self.wrapper.get_num() + 2

class AddThree(Num):
    def __init__(self, wrapper):
        self.wrapper = wrapper
    
    def get_num(self):
        return self.wrapper.get_num() + 3
    

n1 = Num(5)
ch1 = AddThree(AddThree(AddThree(AddTwo(n1))))
# ch2 = AddTwo(n1)
print(ch1.get_num())
# print(ch2.get_num())