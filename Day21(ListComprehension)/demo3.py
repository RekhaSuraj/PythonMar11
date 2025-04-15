# List comprehension - It provides a shorter syntax, to create a new list based on an existing list
# syntax : [Expression for item in iterable]

# print numbers from 1 to 10 and put it in a list
# general for loop where we append items into a new list

# normal method
# new_list = []
# for i in range(1,10):
# 	new_list.append(i)

# print(new_list)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# using list comprehension

list1 = [i for i in range(1,10)]
print('list comprehension:',list1)
# list comprehension: [1, 2, 3, 4, 5, 6, 7, 8, 9]








