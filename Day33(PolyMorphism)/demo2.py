# A base class: Vehicle with a method speed().
# Two derived classes: Truck and Car, both overriding the speed() method.
# This is runtime polymorphism:
# The method speed() behaves differently depending on the object calling it (Truck, Car, or Vehicle).
# Method calls are resolved at runtime — that's why it’s called dynamic method dispatch


class Vehicle:

    def speed(self):
        print('Speed of vehicle is 100kmph')

class Truck(Vehicle):

    def speed(self):
        print('Truck speed is 80kmph')
        super().speed()

class Car(Vehicle):

    def speed(self):
        print('Car speed is 150kmph')
        Truck().speed()


obj_Car = Car()
obj_Car.speed()

# Car speed is 150kmph
# Truck speed is 80kmph
# Speed of vehicle is 100kmph