class ParkingSpot:
    def __init__(self, type, spot_number):
        self.type = type
        self.spot_number = spot_number
        self.parked_vehicle = None
        
    def is_available(self):
        return True if self.parked_vehicle is None else False
    
    def park_vehicle(self, vehicle):
        self.parked_vehicle = vehicle
    
    def unpark_vehicle(self):
        self.parked_vehicle = None
        
    def get_vehicle_type(self):
        return self.type.name
    
    def get_parked_vehicle(self):
        return self.parked_vehicle
    
    def get_spot_number(self):
        return self.spot_number
            