# Instance methods
# Calling Instance Variables by using Instance method
# Instance method: Used to access or modify the object state. If we use instance variables inside a method,
# such methods are called instance methods. It must have a self parameter to refer to the current object.

# self: The first argument self refers to the current object.
# It binds the instance to the __init__() method.
# It’s usually named self to follow the naming convention.

class Mobile:

    def __init__(self,Name, RAM, Color, Price,Mfg):
        self.m_name = Name
        self.m_RAM = RAM
        self.m_color = Color
        self.m_Price = Price
        self.m_Mfg = Mfg

    # Instance method - Fetching all the instance variables and displaying
    def display(self):
        print(f'Name:{self.m_name}')
        print("RAM",self.m_RAM)
        print("Color:",self.m_color)
        print("Price:",self.m_Price)
        print("ManufactureDate:",self.m_Mfg)

# Instance of the class creation 1
obj_Mobile = Mobile("Samsung",8,"White",30000,2025)
obj_Mobile.display()
print(type(obj_Mobile))
# <class '__main__.Mobile'>
print()

# Instance of the class creation 2
obj_Mobile1: Mobile = Mobile("Apple",8,"Black",50000,2025)
obj_Mobile1.display()

# Name:Samsung
# RAM 8
# Color: White
# Price: 30000
# ManufactureDate: 2025

# Name:Apple
# RAM 8
# Color: Black
# Price: 50000
# ManufactureDate: 2025