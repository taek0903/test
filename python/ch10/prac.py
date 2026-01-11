print('1-------------------')
import random
clovers = ['클로버1','클로버2','클로버3']
print(random.sample(clovers,2))

print('2-------------------')
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
car = Car(4,3000)
print(car.wheel)
print(car.price)

print('3-------------------')
class Bicycle(Car):
    def __init__(self, year, wheel, price):
        super().__init__(wheel, price)
        self.year=year
bicycle = Bicycle(2021,2,100)
print(bicycle.year)
print(bicycle.wheel)
print(bicycle.price)

print('4-------------------')
class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.year=year
        self.drivetrain=drivetrain
bicycle=Bicycle(2021, 2, 100, "시마노")
print(bicycle.drivetrain)

print('5-------------------')
class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.year=year
        self.drivetrain=drivetrain
    def info(self):
        print(f"year:{self.year}")
        print(f"wheel:{self.year}")
        print(f"price:{self.price}")
bicycle=Bicycle(2021,2,100,"시마노")
bicycle.info()

print('6-------------------')
class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.year=year
        self.drivetrain=drivetrain
    def info(self):
        print(f"year:{self.year}")
        print(f"wheel:{self.year}")
        print(f"price:{self.price}")
        print(f"drivetrain:{self.drivetrain}")
bicycle=Bicycle(2021,2,100,"시마노")
bicycle.info()