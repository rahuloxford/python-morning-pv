class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_details(self):
        print(f"details of {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine

    def vehicle_details(self):
        print(f"details of {self.brand} {self.model}")
        print(f"Car engine: {self.engine}")

car1 = Car("BMW", "M5", "V12 petrol")
car1.vehicle_details()
