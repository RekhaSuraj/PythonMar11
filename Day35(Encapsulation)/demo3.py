# Protected:
# Protected members are those members of the class that cannot be accessed
# outside the class but can be accessed from within the class and its subclasses.
# To accomplish this in Python, just follow the convention by prefixing the name of the member by
# a single underscore “_”.
# By convention, it means:
# 🔹 "This is meant for internal use only. Please don't access it outside the class or subclass."
# 🔹 But technically, Python still allows access — it's just a warning to developers.

class Employee:

    def __init__(self,Name,Salary):
        self._name = Name #protected variable 1
        self._salary = Salary #protected variable 2

    #protected method(instance method)
    def _display(self):
        print(f'Name:{self._name}\nSalary:{self._salary}')


class Manager(Employee):

    #public method accessing protected method from a subclass
    def show(self):
        self._display()
        # super()._display()

# Accessing public method of child class
obj_Manager = Manager('Akshaya',2000000)
obj_Manager.show()
print()

# Technically, you can still access protected members from outside (not recommended)
obj_Manager._display()
# Name:Akshaya
# Salary:2000000
print()
print(obj_Manager._name)