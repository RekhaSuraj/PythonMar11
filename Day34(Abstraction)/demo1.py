from abc import ABC, abstractmethod

# abstraction:


# Declaration
# Implementation


# Parent class ---->Polygon : Noofside, Area, perimeter

# Child class ---->  Triangle: Noofsides(3), Area, Perimeter

# Rectangle :   Noofside(4),Area, Perimeter

# An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation.
# While we are designing large functional units we use an abstract class.
# When we want to provide a common interface for different implementations of a component, we use an abstract class.


# Why use Abstract Base Classes :
# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.
# This capability is especially useful in situations where a third-party is going to provide implementations,
# such as with plugins, but can also help you when working in a large team or with a large code-base
# where keeping all classes in your mind is difficult or not possible.

# How Abstract Base classes work :
# By default, Python does not provide abstract classes.
#  Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
#  ABC works by decorating methods of the base class as abstract and then registering concrete classes as
# implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.


class School(ABC):

    @abstractmethod
    def login_time(self):
        pass

    @abstractmethod
    def logout_time(self):
        pass

# obj_School = School()
# TypeError: Can't instantiate abstract class School without an implementation for abstract methods 'login_time', 'logout_time'

class DPS(School):

    def login_time(self):
        print('Login time is 8AM')

    # def logout_time(self):
    #     print('Logout time is 5PM')
# TypeError: Can't instantiate abstract class DPS without an implementation for abstract method 'logout_time'

obj_DPS = DPS()
obj_DPS.login_time()
obj_DPS.logout_time()

# Login time is 8AM
# Logout time is 5PM

# IMP Note: In abstraction, we have to implement all abstract methods from parent class in the child class, otherwise
# we will get error like this
# TypeError: Can't instantiate abstract class DPS without an implementation for abstract method 'logout_time'