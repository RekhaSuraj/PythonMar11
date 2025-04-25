# Hierarchical inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say one parent class and multiple child classes.

class A:
    i = 10

class B(A):
    pass

class C(A):
    pass

ob_B = B()
print(ob_B.i)
# 10
ob_C = C()
print(ob_C.i)
# 10