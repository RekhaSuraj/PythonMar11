# Multilevel inheritance
# In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C.
#  A is the superclass, B is the child class of A, C is the child class of B. In other words,
#  we can say a chain of classes is called multilevel inheritance.

class A:
    i = 10

class B(A):
    j = 20

class C(B):
    pass

ob1 = C()
print(ob1.i)
print(ob1.j)
# 10
# 20
