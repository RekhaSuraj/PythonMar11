# For loop in a tuple

t1 = (11,22,33,44,55,66)
for m in t1:
	print(m)


# 11
# 22
# 33
# 44
# 55
# 66

# For loop used in a set
print('****'*10)
s1 = {10,20,30,'hi','hello'}
for s in s1:
	print(s)


# hello
# 20
# 10
# hi
# 30

# For loop used in a string
print('****'*10)
str1 = 'Hello World'

for p in str1:
	print(p)


# H
# e
# l
# l
# o
 
# W
# o
# r
# l
# d

print('******')
# For loop used in a dictionary
dict1 = {1:'abc',2:'xyz',3:'lmn'}

# looping through keys
for k in dict1:
	print(k)


# 1
# 2
# 3

# Looping through all items
print('**********')
for l in dict1.items():
	print(l)

# (1, 'abc')
# (2, 'xyz')
# (3, 'lmn')

# Looping through only values
print('**********')
for m in dict1:
	print(dict1[m])

# abc
# xyz
# lmn

# Looping through both keys and values
print('**********')
for k,v in dict1.items():
	print(v)

# abc
# xyz
# lmn