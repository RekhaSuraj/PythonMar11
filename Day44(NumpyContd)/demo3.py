import numpy as np

# 2d array from user
rows = int(input('Enter no. of rows'))
columns = int(input('Enter no. of columns'))
nd1 = np.ndarray(shape=[rows,columns],dtype=int)

for i in range(rows):
    for j in range(columns):
        nd1[i][j]= int(input('Enter Element:'))

print(nd1)

# Enter no. of rows3
# Enter no. of columns3
# Enter Element:1
# Enter Element:2
# Enter Element:3
# Enter Element:4
# Enter Element:5
# Enter Element:6
# Enter Element:7
# Enter Element:8
# Enter Element:9
#    c0 c1 c2
# [r0[1 2 3]
#  r1[4 5 6]
#  r2[7 8 9]]

# 3 rows, 4 cols
#      c0   c1  c2  c3
# [r0[  1   2   3   4]
#  r1[  5   6   7   8]
#  r2[910  11  12  13]]