
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def details(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Bike(Vehicle):
    def details(self):
        print(f"Bike: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, launchyear, color):
        Vehicle.__init__(self, brand, model)
        self.launchyear = launchyear
        self.color = color

    def details(self):
        print(f"Car details of: {self.brand} {self.model}")
        print(f"Launched in year: {self.launchyear}")
        print(f"Color of the car is: {self.color}")

bmw = Car("BMW", "M5", 2015, "red")
bmw.details()

honda = Bike("Honda", "CB350")
honda.details()

