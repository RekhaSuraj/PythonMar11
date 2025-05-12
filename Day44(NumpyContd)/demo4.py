import numpy as np

n1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(n1)
#      c0 c1 c2 c3
# [r0[ 1  2  3  4]
#  r1[ 5  6  7  8]
#  r2[ 9 10 11 12]]

print(n1.shape)
# (3, 4)
print(n1.ndim)
# 2
print(n1.size)
# 12

# print 2 from the above array
print(n1[0][1])
# 2

print(n1[1][2])
# 7

print(n1[2][3])
# 12


