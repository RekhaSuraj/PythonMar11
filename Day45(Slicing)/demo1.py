import numpy as np
# Slicing
# 1d slicing
l1 = [1,2,3,4,5,6,7,8]
# syntax: [start:stop:step]

n1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print('Shape:',n1.shape)
print('Dimension:',n1.ndim)
print('Size:',n1.size)
print(n1)

# Shape: (3, 5)
# Dimension: 2
# Size: 15

#     c0 c1 c2 c3 c4
# [r0[ 1  2  3  4  5]
#  r1[ 6  7  8  9 10]
#  r2[11 12 13 14 15]]

# 4 5
# 14 15


 # syntax: [rows_slicing,column_slicing]
# syntax: [start:stop:step, start:stop:step]

print()
# [[1 2 3 4 5]]
print(n1[0:1,::])
print(n1[0])
# 7
print(n1[1][1])

print()
print(n1[0:2,1:3])
# [[2 3]
#  [7 8]]

print()
print(n1[0:2,0::3])
# [[1 4]
#  [6 9]]

print()
print(n1[0::2,3::])
# [[ 4  5]
#  [14 15]]