
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f"Employee name: {self.name}")
        print(f"Employee age: {self.age}")
        print(f"Employee salary: {self.salary}")


mohan = Employee("Mohan Kumar", 19, 40000)
