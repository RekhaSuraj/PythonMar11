# index() - Returns the index position of the value specified
# syntax: index(value)
list1 = [20,'hi',30,'hello','welcome', 20]
print(list1.index('welcome',0,5))
# 4

# Fetch the values based on index position
print(list1[4])
# welcome

# We can replace a value in a list without using replace() just by assigning new value to the list based on index
list1[4] = 'python'
print(list1)
# [20, 'hi', 30, 'hello', 'python']

# count() - Returns the count or Return number of occurrences of value in the list
print(list1.count(20))
# 2

# clear() - clears all the elements from the list and will retain an empty list
list1.clear()
print(list1)






