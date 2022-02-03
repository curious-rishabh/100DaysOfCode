# Understanding OOP with freecodecamp
# Day 11 of 100DaysOfCode [Part 2]

# Inheritance
from oops_with_freecodecamp import Item

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity = 1,broken_phones=0):
        # Call to super function to have access to all attibutes/methods
        super().__init__(name, price,quantity)

        # Run validations to received arguments
        assert broken_phones >= 0, f"Broken Phone {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # add instance to list
        Phone.all.append(self)

phone1 = Phone("OnePlus", 50000, 1, 2)
phone1.name = "Apple"
print(phone1.calculate_total_price())
print(phone1.name)
print(Item.all)
print(Phone.all)