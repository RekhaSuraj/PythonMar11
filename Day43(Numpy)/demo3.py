import numpy as np

# 2d numpy array
n1 = np.array([[1,2,3],[4,5,6]])
print(n1)
# [
#     [1 2 3]
#     [4 5 6]
# ]
print(n1.shape)
# (2,3)
print(n1.ndim)
# 2
print()
n2 = n1.reshape(3,2)
print(n2)

# [[1 2]
#  [3 4]
#  [5 6]]