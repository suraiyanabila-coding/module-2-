class Student:

    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        self.marks = []

    def add_marks(self, *marks):
        self.marks.extend(marks)

    def calculate_result(self):
        if len(self.marks) == 0:
            return 0

        total = sum(self.marks)
        return round(total / len(self.marks), 2)

    def display_info(self):
        print("\n--- Student Information ---")
        print("Name       :", self.name)
        print("Student ID :", self.student_id)
        print("Email      :", self.__email)
        print("Age        :", self.age)
        print("Department :", self.department)
        print("Result     :", self.calculate_result())

    def get_student_type(self):
        return "Student"


class UndergraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"


class GraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"


student1 = Student(
    "Shanta",
    "S101",
    "shanta@gmail.com",
    20,
    "CSE"
)

student2 = UndergraduateStudent(
    "Rafi",
    "U201",
    "rafi@gmail.com",
    21,
    "CSE",
    4
)

student3 = GraduateStudent(
    "Nusrat",
    "G301",
    "nusrat@gmail.com",
    25,
    "CSE",
    "Machine Learning"
)


student1.add_marks(80, 85, 90)

student2.add_marks(75, 80, 85, 90)

student3.add_marks(90, 88, 95)


student1.display_info()
print("Type:", student1.get_student_type())

student2.display_info()
print("Semester:", student2.semester)
print("Type:", student2.get_student_type())

student3.display_info()
print("Research Topic:", student3.research_topic)
print("Type:", student3.get_student_type())


students = [student1, student2, student3]

print("\n--- Polymorphism ---")

for student in students:
    print(student.get_student_type())