class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department

    def display_info(self):
        print(self.name, self.student_id, self.__email)

    def calculate_result(self, marks, bonus=0):
        return sum(marks) / len(marks) + bonus

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


student1 = UndergraduateStudent(
    "Rahim", "101", "rahim@gmail.com", 22, "CSE", 6
)

student2 = GraduateStudent(
    "Sara", "102", "sara@gmail.com", 24, "CSE", "AI"
)

student1.display_info()
print(student1.get_student_type())

student2.display_info()
print(student2.get_student_type())