# Method Overloading

class Arithmetic_Tool:

    def add(self,x,y):
        return x+y


    def add(self,x,y,z):
        return x+y+z

    # Default arguments
    def add(self,x,y,z=0,m=0):
        return x+y+z+m


obj = Arithmetic_Tool()
print(obj.add(5,6))
# TypeError: Arithmetic_Tool.add() missing 2 required positional arguments: 'z' and 'm'