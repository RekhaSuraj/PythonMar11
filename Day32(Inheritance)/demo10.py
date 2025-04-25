class Manager:

    def __init__(self,Name, Age, Gender, Salary, Teams, Projects):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.salary = Salary
        self.teams = Teams
        self.projects = Projects


    def display(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n Salary:{self.salary}\n Teams:{self.teams}\n Projects:{self.projects}')


class Employee:

    def __init__(self,Name,Age,Gender,Salary,Technology):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.salary = Salary
        self.technology = Technology



    def display(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Gender:{self.gender}\n Salary:{self.salary}\n Technology:{self.technology}')


obj_Manager = Manager("Swaroop",25,"Male",100000,5,["Amazon","Flipkart","Myntra","Swiggy"])
obj_Manager.display()
print()
obj_Employee = Employee("Rama",200,"Male",50000,"Python")
obj_Employee.display()

# Name:Swaroop
#  Age:25
#  Gender:Male
#  Salary:100000
#  Teams:5
#  Projects:['Amazon', 'Flipkart', 'Myntra', 'Swiggy']
#
# Name:Rama
#  Age:200
#  Gender:Male
#  Salary:50000
#  Technology:Python