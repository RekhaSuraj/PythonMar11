import numpy as np
import array

a1 = array.array('i',[1,2,3,4,5])
a2 = array.array('i',[5,6,7,8,9])

# zip() - In python, the zip() function is used to combine two or more iterables(such as lists or tuples)
# element wise, creating pairs (or tuples) or corresponding elements.
# It stops when the shortest iterable is exhausted.


# Normal python
def prod_function(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1*v2
        # print(result)
    print(result)

prod_function(a1,a2)
# 115

# dot operation - The dot product of 2 vectors is essentially the sum of the products of their corresponding elements.
print()
print(np.dot(a1,a2))
# 115