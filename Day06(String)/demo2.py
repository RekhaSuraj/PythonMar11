# Type casting - conversion - From string to integer
n1 = '30'
print('Before conversion',type(n1))
# Before conversion <class 'str'>

s1 = int(n1)
print(s1)
# 30

print('After conversion',type(s1))
# After conversion <class 'int'>


# s1 = 'hello'
# n2 = int(s1)
# print(n1)
# ValueError: invalid literal for int() with base 10: 'hello'