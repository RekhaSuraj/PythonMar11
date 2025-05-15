import numpy as np

z1 = np.zeros(10,dtype='bool')
print(z1)
# Return a new array of given shape and type, filled with zeros
# [False False False False False False False False False False]

o1 = np.ones(5, dtype='bool')
print(o1)
# [ True  True  True  True  True]

# Extract values based on condition:
l1 = [1,2,3,4,5,6,7,8]
# print(l1>3)
# TypeError: '>' not supported between instances of 'list' and 'int'

n1 = np.array([1,2,3,4,5,6,7,8])
print(n1+1)
# [2 3 4 5 6 7 8 9]

print(n1*2)
# [ 2  4  6  8 10 12 14 16]

print(n1>3)
# [False False False  True  True  True  True  True]
print(n1[n1 > 3])
# [4 5 6 7 8]

