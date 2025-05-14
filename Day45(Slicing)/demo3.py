import numpy as np
# 3d Slicing

# Slicing 3-D

#     i   ,    j   ,  c
# [[[],[]],[[],[]],[[],[]]]

# syntax : [start : stop : step, start : stop : step, start : stop: step]

nd1 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]],[[17,18,19,20],[21,22,23,24]]])
print(nd1.shape)
print(nd1.ndim)
print(nd1.size)
print(nd1)

# (3, 2, 4)
# 3
# 24

#           c0 c1 c2 c3
# [i0-->[j0[ 1  2  3  4]
#        j1[ 5  6  7  8]]
#
#  i1-->[j0[ 9 10 11 12]
#        j1[13 14 15 16]]
#
#  i2-->[j0[17 18 19 20]
#        j1[21 22 23 24]]]



# [[[ 1  2  3  4]]]
print(nd1[0:1,0:1,::])

print()

print(nd1[::,0:1:,1::2])
# [[[ 2  4]]
#
#  [[10 12]]
#
#  [[18 20]]]


print()
# [[[ 5  6]]
#
#  [[21 22]]]

print(nd1[0::2,1::,0:2])

# hw - -ve slicing - same outputs as above