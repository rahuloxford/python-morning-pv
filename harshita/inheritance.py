class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def printname(self):
        return f"{self.fname} {self.lname}"


class Student(Person):
    def __init__(self, fname, lname, age, semester, fees):
        super().__init__(fname, lname, age)
        self.semester = semester
        self.fees = fees

    def student_details(self):
        print(f"{self.printname()} is {self.age}")
        print(f"In semester {self.semester} and his fees is {self.fees}")

mohan = Student("Mark", "Olsen", 28, 3, 40000)
mohan.student_details()

