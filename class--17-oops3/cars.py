
class Car:
    def __init__(self, brand, model, engine, color, mileage):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.color = color
        self.mileage = mileage

    def car_details(self):
        print(f"Car brand: {self.brand}")
        print(f"Car model: {self.model}")
        print(f"Car engine: {self.engine}")
        print(f"Car color: {self.color}")
        print(f"Car mileage: {self.mileage}")

    def averageSpeed(self, speed, timeInHour):
        print(f"Your average speed is {speed * timeInHour}")

    def distanceToEmpty(self, fuel):
        print(f"{self.brand} {self.model} can travel for {fuel * self.mileage}km with the fuel left")



bmw = Car("BMW", "M5", "v8 petrol engine", "Matte", 13.25)

bmw.car_details()
bmw.distanceToEmpty(15)

toyota = Car("Toyota", "Camry", "3 ltr petrol engine", "White", 19)

toyota.car_details()
toyota.distanceToEmpty(13)



