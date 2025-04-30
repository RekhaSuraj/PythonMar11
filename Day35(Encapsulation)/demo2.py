# Accessing public method from a child class
class Employee:
    def __init__(self,Name,Age,Salary):
        self.name = Name #public variable1
        self.age = Age #public variable2
        self.salary = Salary #public variable3

    #public method (instance method)
    def display(self):
        print(f'Name:{self.name}\nAge:{self.age}\nSalary:{self.salary}')

class Manager(Employee):

    def show(self):
        self.display()
        # super().display()

obj_Manager = Manager("Test1",30,100000)
obj_Manager.show()

# Name:Test1
# Age:30
# Salary:100000