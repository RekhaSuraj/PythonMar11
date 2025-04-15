# List methods - concatenate 2 lists using + operator
list1 = [20,40,'hi',50,'hello']
list2 = [11,22,33,44]

list3 = list1 + list2
print(list3)
# [20, 40, 'hi', 50, 'hello', 11, 22, 33, 44]

# print(help(list))
# append() - Append/Add object to the end of the list.
list1.append(60)
print(list1)
# [20, 40, 'hi', 50, 'hello', 60]

# list1.append(list2)
# print(list1)
# [20, 40, 'hi', 50, 'hello', 60, [11, 22, 33, 44]]

# extend() - Extend list by appending/adding elements from the iterable.
# Here list2 is added to list1.
list1.extend(list2)
print('list1',list1)
print('list2',list2)

# list1 [20, 40, 'hi', 50, 'hello', 60, 11, 22, 33, 44]
# list2 [11, 22, 33, 44]

# pop() - Remove and return item at index (default last)
n1 = list1.pop(3)
print(n1)
# 50
print(list1)
# [20, 40, 'hi', 'hello', 60, 11, 22, 33, 44]

# remove() - Remove first occurrence of value
list1.remove('hello')
print(list1)
# [20, 40, 'hi', 60, 11, 22, 33, 44]

# list1.clear()
# list1.index()
# list1.count()

list2 = list1.copy()

