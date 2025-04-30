class Employee:

    def __init__(self,Name,Age,Salary,Gender,Country,Profession):
        self.__name = Name #private var 1
        self.__age = Age #private var 2
        self.__salary = Salary #private var 3
        self._gender = Gender #protected var 1
        self.country = Country #public var 1
        self._profession = Profession #protected var 2


obj = Employee('Seetha',200,200000,"Female","India","SocialService")

print(obj.country) #public
print(obj._gender) #protected
print(obj._profession) #protected
# India
# Female
# SocialService

# AttributeError: 'Employee' object has no attribute '__name'
# private members cannot be accessed, but name mangling can be done
# print(obj.__name)
print(obj._Employee__name)
# Seetha

# Public vs Protected vs Private identifiers in Python:
#
#
# Access Modifier | Syntax Example    | Access Level                              | Accessible in Subclass?               | Accessible Outside Class?            | Internal Name?
# Public          | self.name         | No restriction (Fully open)               | ✅ Yes                                |✅ Yes                                | name
# Protected       | self._name        | Meant for internal use (by convention)    | ✅ Yes                                | ⚠️ Yes (but not recommended)            | _name
# Private         | self.__name       | Strongest level of hiding                 | ⚠️ Difficult (requires name mangling) | ⚠️ Difficult (via name mangling)   | _ClassName__name
