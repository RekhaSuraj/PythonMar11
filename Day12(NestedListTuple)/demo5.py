# Tuple : Tuple is a Built-in datatype in python
# It is used to store multiple values with in a single unit to Assign to a variable name
# Tuple denoted by round braces / Paranthesis  ( )
# Tuples are immutable - Cannot be modified(Changed) once created

# There are two ways to create a tuple
# Type : 1  using the Paranthesis
t1 = (10,20,30,40) #homogeneous
print(type(t1))
# <class 'tuple'>
print(t1)
# (10, 20, 30, 40)

# Creation of an empty tuple
t2 = ()
print(type(t2))
# <class 'tuple'>

# Creation of tuple using a constructor
t3 = tuple((10,20,40,50,60,'hi',45.5,6+7j,20)) # heterogeneous
print(type(t3))
# <class 'tuple'>

# Supports indexing - Fetch values based on index positions
print(t3[5])
# hi

print(t3[2])
# 40




