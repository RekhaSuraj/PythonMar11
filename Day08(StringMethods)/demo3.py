v1 = "Hello World"
# alpha() - Returns True if the string has only alphabets(not even space,special character, numbers)
# Return True if the string is an alphabetic string, False otherwise
print(v1.isalpha())
# False

v2 = "HelloWorld"
print(v2.isalpha())
# True

# isdigit() - Return True if the string is a digit string, False otherwise
# Returns True if a string contains only digits(numbers)
print(v2.isdigit())
# False

s1 = '1234'
print(s1.isdigit())
# True

s2 = 'Hello123l'
print(s2.isdigit())
# False

# index()
print(s2.index('e'))
# 1

print(s2.index('l'))
# 2

print(s2.index('l',3))
# 3

print(s2.index('l',4,9))
# 8

# print(s2.index('l',4,8))
print(s2.index('z'))
# ValueError: substring not found - l is present in 8th index, it is not present between 4th and 7th indexes

