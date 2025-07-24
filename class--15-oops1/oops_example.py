
class Human:
    pass

rohan = Human()

class Car:
    engine = ""
    mileage = 0

    def race(self):
        print("car is racing..")


bmw = Car()
audi = Car()
vw = Car()
bmw.engine = "v8 petrol engine"
vw.engine = "2 ltr diesel engine"
print(bmw.engine)
print(audi.engine)
print(vw.engine)

Car.race(vw)
vw.race()
bmw.race()
