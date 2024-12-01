class Guest:
    def __init__(self, guest_id, name, email, phone_num):
        self._id = guest_id
        self._name = name
        self._email = email
        self._num = phone_num
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def num(self):
        return self._num