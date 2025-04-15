s1 = {'surendra',6+7j,'chethan','swaroop',50.5}
s2 = {10,20,30}
s1.update(s2)
print('s1',s1)
# s1 {50.5, 'swaroop', 20, 'chethan', 10, (6+7j), 'surendra', 30}

print('s2',s2)
# s2 {10, 20, 30}

s1.update({5,55,555})
print(s1)
# {5, 'swaroop', 10, 555, 'chethan', 'surendra', 50.5, 20, 55, (6+7j), 30}

print('*****'*10)
# difference(iterable) - Return the difference of two or more sets as a new set.
# (i. e. all elements that are in this set but not the others.)
A = {1,2,3,4}
B = {1,2,3}

C = A.difference(B)
print(C)

A.difference_update(B)
print('A',A)
# A {4}
print('B',B)
# B {1, 2, 3}

# When both sets have same values, difference will return an empty set
X = {10,20,30}
Y = {10,20,30}
Z = X.difference(Y)
print(Z)
# set()