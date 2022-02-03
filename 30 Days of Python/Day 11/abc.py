# Abstract class
# Day 11 of 100DaysOfCode

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class can't create object, While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class"""

    @abstractmethod
    def printarea(self):
        pass

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.breadth = 10

    # have to define printarea to create object
    def printarea(self):
        return self.length * self.breadth

rec1 = Rectangle()
print(rec1.printarea())