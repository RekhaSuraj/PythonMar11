# Swapping without using 3rd variable

a = 10
b = 20
print("Before swap")
print("a",a)
print("b",b)
# Before swap
# a 10
# b 20
a = a + b #a=30
b = a - b #b=30-20 = 10
a = a - b #a = 30-10 = 20

print("After swap")
print("a",a)
print("b",b)
# After swap
# a 20
# b 10

