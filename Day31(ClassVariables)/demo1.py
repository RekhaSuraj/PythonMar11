# Class Variable:
# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

class Student:
    # Class varaible
    school_Name = "RavindraBharathiGovtSchool"

    def __init__(self,Name, Age, Class, Gender):
        self.name = Name
        self.age = Age
        self.classStudent = Class
        self.gender = Gender


    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Class: {self.classStudent}')
        print(f'Gender: {self.gender}')
        print(f'School: {self.school_Name}') # access class variable in an instance method
        # Student.school_Name # can be accessed using classname.<class_variable>


ob1 = Student("Surendra",15,10,"Male")
ob2 = Student("Swaroop",10,5,"Male")
ob3 = Student("Chethan",5,1,"Male")
ob4 = Student("Seetha",20,12,"Female")
ob5 = Student("Rekha",16,10,"Female")

all_objs = [ob1,ob2,ob3,ob4,ob5]

for var in all_objs:
    print(f' Name:{var.name}')
    print(f'Age:{var.age}')
    print(f'Class:{var.classStudent}')
    print(f'Gender:{var.gender}')
    print(f'SchoolNAme:{var.school_Name}')
    print()

# Name:Surendra
# Age:15
# Class:10
# Gender:Male
# SchoolNAme:RavindraBharathiGovtSchool
#
#  Name:Swaroop
# Age:10
# Class:5
# Gender:Male
# SchoolNAme:RavindraBharathiGovtSchool
#
#  Name:Chethan
# Age:5
# Class:1
# Gender:Male
# SchoolNAme:RavindraBharathiGovtSchool
#
#  Name:Seetha
# Age:20
# Class:12
# Gender:Female
# SchoolNAme:RavindraBharathiGovtSchool
#
#  Name:Rekha
# Age:16
# Class:10
# Gender:Female
# SchoolNAme:RavindraBharathiGovtSchool






