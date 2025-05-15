import numpy as np
# Negative slicing

n1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(n1.shape)
print(n1.ndim)
print(n1)

# (3, 4)
# 2
#    -c4 -c3 -c2 -c1
# [-r3[ 1  2  3  4]
#  -r2[ 5  6  7  8]
#  -r1[ 9 10 11 12]]

# print -ve slicing
# [[ 9 10 11 12]]
print(n1[-1:,::])


print()
# [[2 3]
#  [6 7]]
print(n1[-3:-1,-3:-1])
