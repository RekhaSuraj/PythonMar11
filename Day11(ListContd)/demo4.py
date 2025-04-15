# copy - Returns a copy of the list
# syntax: list.copy()
l1 = [10,20,30,40]
print('l1',l1)
# l1 [10, 20, 30, 40]
l2 = l1.copy()
print('l2',l2)
# l2 [10, 20, 30, 40]

print(id(l1))
print(id(l2))
# 2003033706880
# 2003034028096

print(l1 is l2)
# False


