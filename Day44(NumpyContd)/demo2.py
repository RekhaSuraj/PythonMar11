import numpy as np
# 1d array taking user input

array_list = int(input('Enter size of the array'))

nd1 = np.ndarray(shape=array_list,dtype=int)

for i in range(array_list):
    nd1[i] = int(input('Enter element:'))

print(nd1)
# [1 2 3 4 5]
l1 = list(nd1)
print(l1)