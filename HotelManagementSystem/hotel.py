from guest import Guest
from reservation import Reservation, ReservationStatus
from payment import CashPayment, CreditCardPayment
from room import RoomStatus, Room
import uuid
from datetime import datetime

class HotelManagementSystem:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.guests = {}
            cls._instance.rooms = {}
            cls._instance.reservations = {}
        return cls._instance
   
    @staticmethod
    def get_instance():
        if HotelManagementSystem._instance is None:
            HotelManagementSystem()
        return HotelManagementSystem._instance
    
    def add_guest(self,guest):
        self.guests[guest.id] = guest
        
    def get_guest(self, guest_id):
        return self.guests.get(guest_id)
    
    def add_room(self,room):
        self.rooms[room.id] = room
        
    def get_room(self,room_id):
        return self.rooms.get(room_id)
    
    def _generate_reservation_id(self):
        return f"RES{uuid.uuid4().hex[:8].upper()}"
    
    def book_room(self, guest, room, check_in_date, check_out_date):
        if room.status == RoomStatus.AVAILABLE:
            room.book()
            reservation_id = self._generate_reservation_id()
            reservation = Reservation(reservation_id, guest, room, check_in_date, check_out_date)
            self.reservations[reservation_id] = reservation
            return reservation
        return None
    
    def cancel_reservation(self, reservation_id):
        reserv = self.reservations.get(reservation_id)
        if reserv:
            reserv.cancel()
            del self.reservations[reservation_id]
            return True
        return False
            
    def check_in(self, reservation_id):
        reserv = self.reservations.get(reservation_id)
        if reserv and reserv.status == ReservationStatus.CONFIRMED:
            reserv.room.checkIn()
        else:
            raise ValueError("Invalid reservation or reservation not confirmed.")
        
    def check_out(self, reservation_id, payment):
        reserv = self.reservations.get(reservation_id)
        if reserv and reserv.status == ReservationStatus.CONFIRMED:
            room = reserv.room
            amount = room.price * (reserv.check_out_date - reserv.check_in_date).days
            
            if payment.process_payment(amount):
                room.checkOut()
                del self.reservations[reservation_id]
            else:
                raise Exception("Payment failed")
        else:
            raise ValueError("Invalid reservation or reservation not confirmed.")