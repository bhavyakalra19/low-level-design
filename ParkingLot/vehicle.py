from enum import Enum

class VehicleType(Enum):
    Car = 0
    Truck = 1
    Motorcycle = 2
    
class Vehicle:
    def __init__(self,num_plate,num):
        self.num_plate = num_plate
        self.type = VehicleType(num)
        
    def get_type(self):
        return self.type.name
    
    def get_num_plate(self):
        return self.num_plate
    
class Car(Vehicle):
    def __init__(self, num_plate):
        super().__init__(num_plate, 0)
        
class Truck(Vehicle):
    def __init__(self, num_plate):
        super().__init__(num_plate, 1)
        
class Motorcycle(Vehicle):
    def __init__(self, num_plate):
        super().__init__(num_plate, 2)