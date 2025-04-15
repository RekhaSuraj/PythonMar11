# Type conversion or typecasting - Converting from one datatype to another datatype is called 
# typecasting/conversion

# Explicit type casting
# Converted type int to float
a = 30
# print('datatype before conversion',type(a))
# datatype before conversion <class 'int'>

b = float(a)
# print(b)
# 30.0 
# print('after conversion',type(b))
# after conversion <class 'float'>

# Convert float to int
# int(object)
v1 = 31.45
print('before conversion',type(v1))
# before conversion <class 'float'>
i1 = int(v1)
print(i1)
# 31
print('after conversion',type(i1))
# after conversion <class 'int'>


v2 = float(8)
print(v2)
# 8.0


v3 = int(56.21)
print(v3)
# 56

