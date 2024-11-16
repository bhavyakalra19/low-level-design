from vehicle import Car, Truck, Motorcycle, VehicleType
from parking_spot import ParkingSpot

class Level:
    def __init__(self, floor, car, truck, motorcycle):
        self.floor = floor
        self.parking_spots = []
        for i in range(car):
            self.parking_spots.append(ParkingSpot(VehicleType(0), i))
        for i in range(truck):
            self.parking_spots.append(ParkingSpot(VehicleType(1), car + i))
        for i in range(motorcycle):
            self.parking_spots.append(ParkingSpot(VehicleType(2), car + truck + i))
            
    def get_floor(self):
        return self.floor
        
    def park_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.get_vehicle_type() == vehicle.get_type() and spot.is_available():
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False
    
    def display_availabily(self):
        for spot in self.parking_spots:
            if spot.is_available():
                print(f"On level {self.floor} spot number {spot.get_spot_number()} is available for {spot.get_vehicle_type()}")