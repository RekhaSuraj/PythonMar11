import numpy as np
# 2d array advanced slicing

n2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(n2.ndim)
print(n2.shape)
print(n2)
# 2
# (3, 4)
#    c0  c1  c2 c3
# [r0[ 1  2  3  4]
#  r1[ 5  6  7  8]
#  r2[ 9 10 11 12]]
print()
# Extract 1 3 5 8 10 11
# Normal Slicing : [start : stop : step, start : stop : step]
# n2[[rows_slicing],[column_slicing]]
print(n2[[0,0,1,1,2,2],[0,2,0,3,1,2]])
# [ 1  3  5  8 10 11]

# Extract 12 3 6 1
print(n2[[2,0,1,0],[3,2,1,0]])
# [12  3  6  1]