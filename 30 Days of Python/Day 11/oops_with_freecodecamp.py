# Understanding OOP with freecodecamp
# Day 11 of 100DaysOfCode

import csv

class Item:
    # class attribute
    pay_rate = 0.9 
    # After 10% discount
    all = []

    # name: str => accept string data type only
    def __init__(self, name: str, price: float, quantity = 1):
        # can use arguments directly
        print(f"Object Created for {name}")

        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self._name = name
        # instance attribute
        self.price = price
        self.quantity = quantity

        # add instance to list
        Item.all.append(self)

    # Property Decorator -> Read only attribute
    @property
    def name(self):
        return self._name
        # Restrict behaviour of user
    
    # Set new value to attribute which are restricted before
    @name.setter
    def name(self,value):
        if len(value) >10:
            raise Exception("The name is too long")
        else:
            self._name = value


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    # Class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('100 Minor Projects in Python/Day 11/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            # creating instances
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity= int(item.get('quantity')),
            )

    # Static method
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            # count out floats that are point zero 
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    
    # Special method to represent object
    def __repr__(self):
        # self.__class__.__name__ => access class name from instance
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"

    # Restrict behaviour by using read only attribute
    # @property
    # def read_only_attribute(self):
    #     return "RB"


item1 = Item("Phone", 25000,1)
item2  = Item("Laptop", 153000,2)

print(item1.name)
print(item1.calculate_total_price())
print(item2.name)
print(item2.calculate_total_price())
print()
item1.apply_discount()
print(item1.price)
item2.apply_discount()
print(item2.price)

# Calling class atrribute
print(f"Pay rate {Item.pay_rate}")

# Bring attribute from class level
print(f"Pay rate from class level {item2.pay_rate}")

# Bring all attributes from class level by using magic attributes-> __dict__
print(Item.__dict__)
# Bring all attributes from instance level
print(item2.__dict__)

# call instance name 
for instance in Item.all:
    print(instance.name)

# Calling class method 
Item.instantiate_from_csv()

# Add all instance to list
print(Item.all)
