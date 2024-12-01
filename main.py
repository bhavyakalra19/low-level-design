from enum import Enum

class VehicleType(Enum):
    Car = 0
    Truck = 1
    Motorcycle = 2
    
class Vehicle:
    def __init__(self,num,num_plate):
        self.type = VehicleType(num)
        self.num_plate = num_plate
        
    def get_type(self):
        return self.type.name
        
    def get_num_plate(self):
        return self.num_plate
    
class Car(Vehicle):
    def __init__(self, num_plate):
        super().__init__(0, num_plate)

class Truck(Vehicle):
    def __init__(self, num_plate):
        super().__init__(1, num_plate)
    
class Motorcycle(Vehicle):
    def __init__(self, num_plate):
        super().__init__(2, num_plate)
        

class ParkingSpot:
    def __init__(self,spot,type):
        self.spot = spot
        self.parked_vehicle = None
        self.type = type
        
    def is_available(self):
        return True if self.parked_vehicle is None else False
    
    def park_vehicle(self,vehicle):
        self.parked_vehicle = vehicle
        
    def unpark_vehicle(self):
        self.parked_vehicle = None
    
    def get_vehicle_type(self):
        return self.type.name
    
    def get_spot_number(self):
        return self.spot
    
    def get_parked_vehicle(self):
        return self.parked_vehicle
    
    
class Level:
    def __init__(self,floor,car,truck,motorcycle):
        self.floor = floor
        self.parking_spots = []
        
        for i in range(car):
            self.parking_spots.append(ParkingSpot(i,VehicleType(0)))
        for i in range(truck):
            self.parking_spots.append(ParkingSpot(i + car,VehicleType(1)))
        for i in range(motorcycle):
            self.parking_spots.append(ParkingSpot(i + car + motorcycle,VehicleType(2)))
            
        
    def park_vehicle(self,vehicle):
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                print(f"Your {vehicle.get_type()} of plate number {vehicle.get_num_plate()} is parked on level {self.floor} and spot is {spot.get_spot_number()}")
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self,vehicle):
        for spot in self.parking_spots:
            if spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False
    
    def display_availability(self):
        for spot in self.parking_spots:
            if spot.is_available():
                print(f"{spot.get_spot_number()} is available on level {self.floor} for {spot.get_vehicle_type()}")
                
                
class Parking:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.levels = []
        return cls._instance

    @staticmethod
    def get_instance():
        if Parking._instance is None:
            Parking()
        return Parking._instance

    def add_level(self,level):
        self.levels.append(level)
    
    def park_vehicle(self,vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        print(f"No parking spot is available for {vehicle.get_type()}")
        return False
    
    def unpark_vehicle(self,vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        print("Your vehicle is not in parking spot")
        
    def display_availability(self):
        for level in self.levels:
            level.display_availability()
            
class ParkingDemo:
    def run():
        parking_lot = Parking.get_instance()
        
        parking_lot.add_level(Level(1,2,2,2))
        parking_lot.add_level(Level(2,2,2,2))
        
        c1 = Car("ABC001")
        c2 = Car("ABC002")
        c3 = Car("ABC003")
        c4 = Car("ABC004")
        c5 = Car("ABC005")
        parking_lot.display_availability()  
        print("------------------------")
        
        parking_lot.park_vehicle(c1)
        parking_lot.park_vehicle(c2)
        parking_lot.park_vehicle(c3)
        parking_lot.park_vehicle(c4)
        parking_lot.park_vehicle(c5)
        
        parking_lot.display_availability()    
        parking_lot.unpark_vehicle(c1)
        print("------------------------")
        parking_lot.display_availability()
    
if __name__ == "__main__":
    ParkingDemo.run()