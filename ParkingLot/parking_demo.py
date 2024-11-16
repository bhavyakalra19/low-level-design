from parking_lot import ParkingLot
from level import Level
from vehicle import Car, Truck, Motorcycle

class ParkingDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        
        parking_lot.add_level(Level(1,2,2,2))
        parking_lot.add_level(Level(2,2,2,2))
        
        c1 = Car("ABC001")
        c2 = Car("ABC002")
        c3 = Car("ABC003")
        c4 = Car("ABC004")
        c5 = Car("ABC005")
        
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