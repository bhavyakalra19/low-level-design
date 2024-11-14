# The Dependency Inversion Principle (DIP) is a principle in object-oriented design 
# that states that “High-level modules should not depend on low-level modules. Both 
# should depend on abstractions“. Additionally, abstractions should not depend on 
# details. Details should depend on abstractions.

from abc import ABC, abstractmethod

class Sender(ABC):
    @abstractmethod
    def send(self):
        pass
    
class EmailSender(Sender):
    def send(self, str):
        print(f"Sending email {str}")
        
class SmsSender(Sender):
    def send(self,str):
        print(f"Sendin sms {str}")
        
class MessageSender:
    def __init__(self, sender):
        self.message_sender = sender
    
    def sender_service(self,message):
        self.message_sender.send(message)
        

e1 = EmailSender()
s1 = SmsSender()

m1 = MessageSender(e1)
m2 = MessageSender(s1)

m1.sender_service("Hello")
m2.sender_service("Hello")