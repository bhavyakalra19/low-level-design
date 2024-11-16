from registration import Registration
from course import Course
from student import Student
from datetime import datetime

class CourseRegistration:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.courses = {}
            cls._instance.students = {}
            cls._instance.registrations = []
        return cls._instance
            
            
    @staticmethod
    def get_instance():
        if CourseRegistration._instance is None:
            CourseRegistration()
        return CourseRegistration._instance
    
    def add_course(self,course):
        self.courses[course.get_name()] = course
        
    def add_student(self,student):
        self.students[student.get_name()] = student
        
    def search_courses(self,query):
        result = []
        for course in self.courses.values():
            if query in course.get_code() or query in course.get_name():
                result.append(course)
        return result
    
    def register_course(self,student,course):
        if course.get_enrolled_students() < course.get_max_capacity():
            registration = Registration(student,course,datetime.now())
            self.registrations.append(registration)
            student.add_course(course)
            course.set_enrolled_students(course.get_enrolled_students() + 1)
            return True
        return False
    
    def get_registered_courses(self,student):
        return student.get_course()