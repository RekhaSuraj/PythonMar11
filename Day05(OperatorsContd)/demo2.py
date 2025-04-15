# Identity operator - Also works on iterables (list, tuple, set, string)
# There are 2 identity operators : is and is not

# is - checks for the id and returns True if both values have same id. That is if both values are pointing
# to the same object in memory

l1 = [10,20,30]
l2 = [10,20,30]

# print(l1 is l2)
# # False

# # syntax : id(var_name)
# print('l1 id:',id(l1))
# # l1 id: 1419381625216

# print('l2 id:',id(l2))
# # l2 id: 1419381627072

# l3 = l1
# print(l1 is l3)
# # True

# print('id of l3',id(l3))
# print('id of l1',id(l1))
# # id of l3 2144430051712
# # id of l1 2144430051712

# # Difference between
# # ==,  is

# str1 = 'hello'
# str2 = 'hello'
# print(str1 is str2)
# # True
# print(id(str1))
# print(id(str2))

# 2514504922240
# 2514504922240

# is not
list3 = [10,'hi',20,'hello']
list4 = [10,'hi',20,'hello']

print('list3',id(list3))
print('list4',id(list4))

# list3 2428887216448
# list4 2428887212864

print(list3 is not list4)
# True

print(l1 is not l2)
# True

