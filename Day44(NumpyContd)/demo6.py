import numpy as np
from datetime import datetime
import array

a1 = array.array('i',[1,2,3,4,5])
a2 = array.array('i',[5,6,7,8,9])

def prod_function(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1*v2
        # print(result)
    # print(result)
    return result


# start = datetime.datetime.now()
# for i in range(100000):
#     prod_function(a1,a2)
# # prod_function(a1,a2)
# end = datetime.datetime.now()
#
# print('Normal python operation Time taken:',end-start)
#
#
# # Numpy dot product method
# start1 = datetime.datetime.now()
# for i in range(100000):
#     np.dot(a1,a2)
# # np.dot(a1,a2)
# end1 = datetime.datetime.now()
# print('Numpy dot product method Time taken:',end1-start1)


start = datetime.now()
for i in range(10000):
    prod_function(a1,a2)
end = datetime.now()
time_taken = end - start
print('normal python',time_taken)

start1 = datetime.now()
for i in range(10000):
    np.dot(a1,a2)
end1 = datetime.now()
time_taken1 = end1 - start1
print('dot function',time_taken1)

# normal python 0:00:00.006238
# dot function 0:00:00.021338

# dot function is taking more time because:
# np.dot() needs to convert array.array to NumPy arrays internally, which incurs overhead.
# Example: np.dot(array.array(...), array.array(...)) is slower than np.dot(np.array(...), np.array(...)).