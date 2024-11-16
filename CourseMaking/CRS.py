from course_registration import CourseRegistration
from course import Course
from student import Student

class CRS:
    @staticmethod
    def run():
        rs = CourseRegistration.get_instance()
        
        c1 = Course("CS01", "Introduction to python", "Martha", 50)
        c2 = Course("CS02", "Introduction to C++", "Jack", 50)
        
        s1 = Student(1, "Bhavya", "bkbkbhavyakalra@gmail.com")
        s2 = Student(2, "Chiransh", "chiranshkalra@gmail.com")
        rs.add_student(s1)
        rs.add_student(s2)
        
        rs.add_course(c1)
        rs.add_course(c2)
        
        rs.register_course(s1,c1)
        rs.register_course(s2,c1)
        rs.register_course(s1,c2)
        for a in rs.get_registered_courses(s2):
            print(a.get_name())
            
if __name__ == "__main__":
    CRS.run()