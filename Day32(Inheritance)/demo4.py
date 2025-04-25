# Single level inheritance
# To inherit parent class - inside the parenthesis, give parent class name:
# Syntax: Ex: class B(A):
# In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.

class A:
    i = 10

class B(A):
    pass

ob1 = B()
print(ob1.i)
# 10