
class Vehicle:
    def move(self):
        print("vehicle is moving...")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    def move(self):
        print("riding...")

class Plane(Vehicle):
    def move(self):
        print("flying...")

car = Car()
bike = Bike()
plane = Plane()

car.move()
bike.move()
plane.move()


