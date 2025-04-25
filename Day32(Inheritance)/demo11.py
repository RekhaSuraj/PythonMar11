# Managaer - Name, Age, Gender, Salary, Teams, Projects
# Employee - Name, Age, Gender, Salary, Technology
#
# Profile - Name, Agen Gender, Salary

class Profile:
    def __init__(self,Name, Age, Gender, Salary):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.salary = Salary



class Manager(Profile):

    def __init__(self,Name, Age, Gender, Salary, Teams, Projects):
        super().__init__(Name,Age,Gender,Salary)
        self.teams = Teams
        self.projects = Projects


    def display(self):
        print(
            f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n Salary:{self.salary}\n Teams:{self.teams}\n Projects:{self.projects}')


class Employee(Profile):
    def __init__(self,Name,Age,Gender,Salary,Technology):
        Profile.__init__(self,Name,Age,Gender,Salary)
        self.technology = Technology


    def display(self):
        print(
            f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n Salary:{self.salary}\n Technology:{self.technology}')


obj_Manager = Manager("Surendra",25,"Male",200000,5,["Amazon","Flipkart","Myntra","Swiggy"])
obj_Manager.display()

print()
obj_Employee = Employee("Seetha",200,"FeMale",50000,"Python")
obj_Employee.display()

# Name:Surendra
#  Age:25
#  Gender:Male
#  Salary:200000
#  Teams:5
#  Projects:['Amazon', 'Flipkart', 'Myntra', 'Swiggy']
#
# Name:Seetha
#  Age:200
#  Gender:FeMale
#  Salary:50000
#  Technology:Python