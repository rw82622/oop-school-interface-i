from Classes.Student import Student
from Classes.Staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students(Student)
        self.staff = Staff.all_staff(Staff)