from multipledispatch import dispatch

class Arithmetic_Tool:

    @dispatch(int,int)
    def add(self,x,y):
        return x+y

    @dispatch(int,int,int)
    def add(self,x,y,z):
        return x+y*z

    @dispatch(int,int,int,int)
    def add(self,x,y,z,m):
        return x+y+z+m

obj = Arithmetic_Tool()
print(obj.add(5,8))
# 13
print(obj.add(1,2,3,4))
# 10
print(obj.add(4,5,6))
# 34

