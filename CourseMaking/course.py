from datetime import datetime

class Course:
    def __init__(self, code, name, instructor, max_capacity):
        self.code = code
        self.name = name
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_student = 0
        
    def set_enrolled_students(self,enrolled_students):
        self.enrolled_student = enrolled_students
        
    def get_code(self):
        return self.code
    
    def get_name(self):
        return self.name
    
    def get_instructor(self):
        return self.name
    
    def get_max_capacity(self):
        return self.max_capacity
    
    def get_enrolled_students(self):
        return self.enrolled_student
            