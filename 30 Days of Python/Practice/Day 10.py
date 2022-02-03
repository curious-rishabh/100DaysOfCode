# Day 9 of 100DaysOfCode Practice

# _____________1_______________
# Creating Classes
class ElectricCar:
    # empty class
    print("New object Created from 1st class")
    pass
tesla = ElectricCar()
# object

# adding attribute
tesla.id = "001"
tesla.model = "S"
tesla.range = "500"
print(tesla.id)

# _____________2_______________
# Using constructor & attributes
# self -> actual object
class SportCar:
    # if we declare arguments in constructor then we have to provide values
    def __init__(self, user, name, model):
        self.id = user
        self.name = name
        self.model = model
        # set default value
        self.milage = 6
        self.seats = 4
        print("New object created!! from 2nd class")

# call attribute by name defined in constructor
lambhorghini = SportCar(2,"Aventador", 2026)
print(lambhorghini.id)

# _____________3_______________
# adding method to class
class LuxuryCar:
    def __init__(self, user, name, model):
        self.id = user
        self.name = name
        self.model = model
        # set default value
        self.milage = 4
        self.seats = 3
        print("New object created!! from 3rd class")

    def sport_mode(self):
        self.seats = 2
        self.milage = 2

rollsroyce = LuxuryCar(2,"Ghost", 2032)

print(rollsroyce.sport_mode())