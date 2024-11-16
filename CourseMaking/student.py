class Student:
    def __init__(self, student_id, name, email):
        self.id = student_id
        self.name = name
        self.email = email
        self.courses = []
        
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_course(self):
        return self.courses
    
    def add_course(self,course):
        self.courses.append(course)