
class Student:
    def __init__(self, name, rno, age):
        self.name = name
        self.rno = rno
        self.age = age

    def student_details(self):
        print(f"Student name: {self.name}")
        print(f"Student rno: {self.rno}")
        print(f"Student age: {self.age}")

student1 = Student("jon walker", 19735, 23)
student2 = Student("peter parker", 47628, 26)

student1.student_details()
student2.student_details()
