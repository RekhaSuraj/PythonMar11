# What is an Array ?
# An array is basically a data structure which can be holds more than one value at a time.
# It is a collection or ordered series of elements of the same type
import array
import numpy as np

# Difference between numpyArray and list

# By default arrays concept is not available in python , instead of we can use list.
# [But, make sure list and Arrays both are not same]

# 1.But in python , we can create arrays in the following 2 ways
# How to import module?
# 1. By using array module
# 2. By using numpy Module

# Python list and Numpy arrays
# 1.Similarities
# 2.Difference
# 3. Advantages of array

# 1.Similarities :
# a). Both can be used to store data
# b). Order will be preserved in both type.(we can access elements using index)
# c). Slicing is also applicable for both
# d). Both are mutable, once we create list or array.


# 2.Difference
# a1). List is In-built data type but numpy array is not in-built, we have to install
# a2).We have to creating number of dimensions in numpy array, it is not possible to make Ndimension in list
# a3).List can hold heterogenous (Multiple data types)
#        but Array can hold only homogenous element
# a4). On arrays we can perform vector operations like 1-D, 2-D, 3-D
# (the operation but we cannot perform vector operations on list).

# 3 . Advantage of Array
# a5). Array consuming less memory
# a6).Array super fast when compared with list.
# a7). Numpy array are more convenient to use while performing mathematical operations


a1 = array.array('i',[1,2,3,4,5])
print(type(a1))
# <class 'array.array'>
print(a1)
# array('i', [1, 2, 3, 4, 5])

nd1 = np.ndarray(shape=[2,3],dtype=int)
print(type(nd1))
# <class 'numpy.ndarray'>

nd2 = np.array([10,20,30,40,50])
print(type(nd2))
# <class 'numpy.ndarray'>
print(nd2.shape)
# (5,)
print(nd2.ndim)
# 1
print(nd2.size)
# 5
