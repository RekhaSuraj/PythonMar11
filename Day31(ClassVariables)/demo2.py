# Update class variable in an instance method and delete class variable
class Employee:

    company = "HAL"
    def __init__(self,Name, idNum):
        self.name = Name
        self.idNumber = idNum

    def display(self):
        print("NAme:",self.name)
        print("IdNum:",self.idNumber)
        print("Company:",self.company)

    # update class variable inside an instance method
    def change_classVar(self,new_Name):
        # self.company = new_Name
        # Delete class variable using class name.<classvariable>
        Employee.company = new_Name
        # print(self.company)


    def delete_classVar(self):
        del self.company
        # del Employee.company


obj_Employee = Employee("ABC",1234)
obj_Employee.display()
obj_Employee.change_classVar("TCS")
print()
obj_Employee.display()

# NAme: ABC
# IdNum: 1234
# Company: HAL
#
# NAme: ABC
# IdNum: 1234
# Company: TCS

obj_Employee.delete_classVar()
obj_Employee.display()
# AttributeError: 'Employee' object has no attribute 'company'
