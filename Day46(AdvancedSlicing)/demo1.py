# Advanced Slicing
import numpy as np

l1 = [1,2,3,4,5,6]
# extract values - 2,3,5,1. Its not possible using slicing

# 1d array
n1 = np.array([1,2,3,4,5,6,7,8,9])
# Extract values 1 3 4 6 9
print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1)
# 1
# (9,)
# 9
# [1 2 3 4 5 6 7 8 9]
# s1 = [1,3,4,6,9]
s2 = [0,2,3,5,8]
print(n1[s2])
# [1 3 4 6 9]
