class Human:
    # special method __init__
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def person_details(self):
        print(f"----------Person details for {self.name}----------")
        print(f"Person name: {self.name}")
        print(f"Person age: {self.age}")
        print(f"Person height: {self.height}")
        print(f"Person weight: {self.weight}")

    def talk(self):
        print(self.name, "is talking..")


# Human() -> constructor (a special function that instanciate the object of a class)
akash = Human("Akash Kushwaha", 23, 5.11, 81)
sachin = Human("Sachin Roy", 22, 5.9, 72)
subodh = Human("Subodh", 24, 5.6, 65)

akash.person_details()
subodh.person_details()
sachin.person_details()


