from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class CashPayment(Payment):
    def process_payment(self, amount):
        return True

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return True