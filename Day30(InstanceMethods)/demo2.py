# Update instance variables using instance methods

class Employee:

    def __init__(self, Name,Gender,Salary,Technology):
        self.name = Name
        self.gender = Gender
        self.salary = Salary
        self.technology = Technology


    # Instance method - display all instance variables
    def show(self):
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Salary:",self.salary)
        print("Technology:",self.technology)


    # Instance method - Update Technology
    def update_technology(self):
        self.technology = "Java"

    # Instance method - Update Salary
    def update_Salary(self,new_Salary):
        self.salary = new_Salary

obj_Employee = Employee("Surendra","Male",100000,"Python")
obj_Employee.show()
print()
# Name: Surendra
# Gender: Male
# Salary: 100000
# Technology: Python

obj_Employee.update_technology()
obj_Employee.show()

# Name: Surendra
# Gender: Male
# Salary: 100000
# Technology: Java
print()
obj_Employee.update_Salary(120000)
obj_Employee.show()

# Name: Surendra
# Gender: Male
# Salary: 120000
# Technology: Java

