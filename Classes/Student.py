from Classes.Person import Person
import csv

class Student(Person):
    students_list = []
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id
    
    @classmethod
    def all_students(self):
        with open("./data/students.csv") as file:
            students = csv.reader(file)
            for row in students:
                if row[0] != "name":
                    Student.students_list.append(row)
        return Student.students_list
    
    
# print(Student.all_students(Student))
# rex = {'name': 'Rex', 'age': 27, 'password': 'i329i4', 'role': 'Student', 'school_id': 1234}    
# student1 = Student(**rex)