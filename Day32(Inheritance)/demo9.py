# Hybrid inheritance
# When inheritance consists of multiple types or a combination of different inheritance is called hybrid inheritance.

class A:
    i = 10

class B(A):
    j = 20

class C(A):
    k = 30

class D(B,C):
    pass

ob1 = D()
print(ob1.i)
print(ob1.j)
print(ob1.k)

# 10
# 20
# 30