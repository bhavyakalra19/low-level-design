# In the original code, we have a MessageSender class that sends 
# notifications through Sender using the Sender class. This tightly 
# couples the MessageSender with the specific email implementation, 
# making it difficult to add new ways of communication to the system.

class Sender():
    def send(self,message):
        print(f"Sending message {message}")

class MessageSender(Sender):
    def __init__(self):
        self.email_sender = Sender()
        
    def send_message(self,message):
        self.email_sender.send(message)
        
m1 = MessageSender()
m1.send_message("Hello")