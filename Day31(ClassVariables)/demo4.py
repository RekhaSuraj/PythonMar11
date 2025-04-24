# Let’s see how to create a factory method using the class method.
# A factory method in Python is a design pattern used to create objects. Instead of calling the constructor (__init__) directly to create an object,
# you use a method (often a @classmethod) that returns an instance of the class — sometimes with custom initialization logic.
#
# Why Use a Factory Method?
# To encapsulate object creation logic
#
# To return different subclasses based on input
#
# To reuse code for multiple ways of creating objects
#
# To give meaningful names to ways of creating an object

from datetime import date
class Student:

    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    @classmethod
    def Calculate_Age(cls,Name, birth_year):
        print(date.today().year)
        age = date.today().year - birth_year
        return cls(Name,age)


    def display_age(self):
        return f'{self.name} age is {self.age}'

# ob1 = Student("Rama",200)

# Alternative constructor @classmethod(Calculate_age)
var = Student.Calculate_Age("Seetha",1990)
print(var.name)
print(var.age)
var.display_age()
# 2025
# Seetha
# 35



