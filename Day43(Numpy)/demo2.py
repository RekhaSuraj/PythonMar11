import numpy as np
import array

l1 = [1,2,3,4,5]
print(type(l1))
# <class 'list'>

a1 = array.array('i',l1)
print(type(a1))
# <class 'array.array'>

# import numpy as np
# syntax : modulename.function()

# print(help(np.array))
n1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(n1)
# [ 1  2  3  4  5  6  7  8  9 10]
print()
# Properties - Getters and Setters
print('Shape',n1.shape)
print('NDim:',n1.ndim)
print('Size:',n1.size)
print('Itemsize:',n1.itemsize)
print('DataType:',n1.dtype)

# Shape (10,)
# NDim: 1
# Size: 10
# Itemsize: 8
# DataType: int64

print()
n2 = np.array([1,2,3,4,5],dtype=float)

print('Shape',n2.shape)
print('NDim:',n2.ndim)
print('Size:',n2.size)
print('Itemsize:',n2.itemsize)
print('DataType:',n2.dtype)

# Shape (5,)
# NDim: 1
# Size: 5
# Itemsize: 8
# DataType: float64

