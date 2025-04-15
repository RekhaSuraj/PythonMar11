# Datatypes
# Number - int, float, complex
# Bool - True, False
# Set
# Dictionary
# Sequence Datatypes - String, List, Tuple

# Number
# int - integer with positive and negative whole numbers. No decimal points

x = 25
print(type(x))
# <class 'int'>

# type() - inbuilt method which gives the datatype of the object specified inside the brackets

y = -39
print(type(y))
# # <class 'int'>

# # float - it has decimal point numbers
f = 4.6
print(type(f))
# # <class 'float'>


f1 = -4.6
print(type(f1))
# # <class 'float'>


c = 6 + 7j
print(c.real)
# 6.0

print(c.imag)
# 7.0

a = 7
b = 9

c1 = complex(a,b)
print(c1)
# (7+9j)

x = True + 5 + 4 + False
print(x)

a1 = 4.5
b1 = 5

res = a1 + b1 # Implicit typecasting
print(res) # Float
# 9.5

l = 30.45
m = int(l)
print(m)

# 30

print(0b1100)
# 12