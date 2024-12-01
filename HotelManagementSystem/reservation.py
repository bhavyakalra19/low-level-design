from enum import Enum
from datetime import date

class ReservationStatus(Enum):
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    
class Reservation:
    def __init__(self, id, guest, room, check_in_date, check_out_date):
        self.id = id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = ReservationStatus.CONFIRMED
        
    def cancel(self):
        if self.status == ReservationStatus.CONFIRMED:
            self.status = ReservationStatus.CANCELLED
            print("Reservation done")
        else:
            print("Reservation not in record")