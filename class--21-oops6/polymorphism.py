
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("vehicle is moving")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying..")

car1 = Car("Audi", "R8")
boat1 = Boat("Ibiza", 738)
plane1 = Plane("Boeing", 787)

car1.move()
plane1.move()
boat1.move()