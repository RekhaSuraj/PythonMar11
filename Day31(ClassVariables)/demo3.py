# class methods
# Class method: Used to access or modify the class state.
# In method implementation, if we use only class variables,
# then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.
# class methods:

# Create Class Method Using @classmethod Decorator
# To make a method as class method, add @classmethod decorator before the method definition, and add cls as the first parameter to the method.
#
# The @classmethod decorator is a built-in function decorator. In Python, we use the @classmethod decorator to declare a method as a class method.
# The @classmethod decorator is an expression that gets evaluated after our function is defined.

# What is a Decorator in Python?
# A decorator in Python is a design pattern that lets you add new behavior to a function or class method without modifying its structure.


# Create Class Method Using @classmethod Decorator
# To make a method as class method, add @classmethod decorator before the method definition, and add cls as the first parameter to the method.


class Employee:

    company = "Infosys"
    def __init__(self,Name, Age):
        self.name = Name
        self.age = Age

    @classmethod
    def cls_company(cls):
        print(cls.company)


# ob1 = Employee("ABC",20)
# print(ob1.name)
# print(ob1.age)

# Class method directly from class, it acts as a constructor
Employee.cls_company()
# Infosys


