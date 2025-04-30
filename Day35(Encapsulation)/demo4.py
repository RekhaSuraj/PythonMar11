# Private :
# Private members are similar to protected members,
# the difference is that the class members declared private should neither be accessed outside
# the class nor by any base class.
# In Python, there is no existence of Private instance variables that cannot be accessed
# except inside a class.
#
# However, to define a private member prefix the member name with double underscore “__”.

class Student:

    def __init__(self, Name, Marks):
        self.__name = Name #private variable 1
        self.__marks = Marks #private variable 2

    #Private method(instance)
    def __display(self):
        print(f'Name:{self.__name}\nMarks:{self.__marks}')

    # Public method
    def show(self):
        self.__display()

obj_student = Student('Rama',95)
obj_student.show()

# Name:Rama
# Marks:95

# If we try to access private members from outside, we get error
# obj_student.__display()
# AttributeError: 'Student' object has no attribute '__display'

# print(obj_student.__name)
# AttributeError: 'Student' object has no attribute '__name'

# Name mangling
# But... (Name Mangling)
# If you really want to (not recommended), you can access it like this:
# syntax : <obj_name>._<class_name>__<attribute/method>
print(obj_student._Student__name)
# Rama

print(obj_student._Student__marks)
# 95

obj_student._Student__display()
# Name:Rama
# Marks:95
