# Multiple inheritance
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.

class A:
    i = 10

class B:
    j = 20

class C(A,B):
    pass

ob1 = C()
print(ob1.i)
print(ob1.j)
# 10
# 20

