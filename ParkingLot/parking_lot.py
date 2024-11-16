from level import Level

class ParkingLot:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.levels = []
        return cls._instance
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_level(self,level):
        self._instance.levels.append(level)
        
    def park_vehicle(self,vehicle):
        for level in self._instance.levels:
            if level.park_vehicle(vehicle):
                print(f"Your {vehicle.get_type()} of number plate {vehicle.get_num_plate()} is parked on {level.get_floor()}")
                return True
        print(f"Parking not available in parking lot")
        return False
    
    def unpark_vehicle(self,vehicle):
        for level in self._instance.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    
    def display_availability(self):
        for level in self._instance.levels:
            level.display_availabily()