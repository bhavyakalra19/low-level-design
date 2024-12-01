from enum import Enum

class RoomType(Enum):
    SINGLE = 'SINGLE'
    DOUBLE = 'DOUBLE'
    DELUXE = 'DELUXE'
    SUITE = "SUITE"
    
class RoomStatus(Enum):
    AVAILABLE = "AVAILABLE"
    BOOKED = "BOOKED"
    OCCUPIED = "OCCUPIED"
    
class Room:
    def __init__(self, id, type, price):
        self.id = id
        self.type = type
        self.price = price
        self.status = RoomStatus.AVAILABLE
        
        
    def book(self):
        if self.status == RoomStatus.AVAILABLE:
            self.status = RoomStatus.BOOKED
            print("Room booked!")
        else:
            print("Room is not availbale!")
        
    def checkIn(self):
        if self.status == RoomStatus.BOOKED:
            self.status = RoomStatus.OCCUPIED
            print("CheckIn completed")
        else:
            print("Room is not booked!")
    
    def checkOut(self):
        if self.status == RoomStatus.OCCUPIED:
            self.status = RoomStatus.AVAILABLE
            print("CheckOut completed!")
        else:
            print("Room is not occupied!")