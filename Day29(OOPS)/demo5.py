# Constructors in Python

# Constructors in Python

# In Python, a constructor is a special type of method used to initialize the object of a Class.
# The constructor will be executed automatically when the object is created. If we create three objects,
# the constructor is called three times and initialize each object.

# The main purpose of the constructor is to declare and initialize instance variables. It can take at least one argument that is self.
#  The __init()__ method is called the constructor in Python. In other words, the name of the constructor should be __init__(self).
# self() - refers to that particular instance of the class

# A constructor is optional, and if we do not provide any constructor, then Python provides the default constructor.
# Every class in Python has a constructor, but it's not required to define it.

# def: The keyword is used to define function.
# __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.

# class Person:

    # def __init__(self):
        # body of the constructor


class Person:

    # Constructor
    def __init__(self, Name, Age, Salary):
        self.P_name = Name # instance variable1
        self.P_Age = Age # instance variable2
        self.P_Salary = Salary #instance variable3

        print(self.P_name)
        print(self.P_Age)
        print(self.P_Salary)


obj_Person = Person("Surendra",25, 500000)
# Surendra
# 25
# 500000



















