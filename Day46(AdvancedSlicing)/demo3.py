import numpy as np

n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n1)

#     -c3 -c2 -c1
# [-r3[1   2   3]
#  -r2[4   5   6]
#  -r1[7   8   9]]

print()
# -ve slicing
# Extract 2 8 5 7
print(n1[[-3,-1,-2,-1],[-2,-2,-2,-3]])
# [2 8 5 7]