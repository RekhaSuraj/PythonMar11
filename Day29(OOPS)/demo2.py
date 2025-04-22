# How do we create a class?
# syntax: using class <class_name>:

# class declaration
class Person:
    # Attributes of the class
    Name = "Swaroop"
    Gender = "Male"
    Profession = "IT"


# How do we create an instance(object for the class) of the class (how do we call this class)
obj_Person = Person()
print(type(obj_Person))
# <class '__main__.Person'>

# Access the attributes of the class
print(obj_Person.Name)
print(obj_Person.Gender)
print(obj_Person.Profession)

# Swaroop
# Male
# IT


