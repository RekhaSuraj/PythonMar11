import numpy as np
from datetime import datetime
import array

a1 = np.array([1,2,3,4,5])
a2 = np.array([5,6,7,8,9])

def prod_function(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1*v2
        # print(result)
    # print(result)
    return result


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

# dot function is taking less time - we have directly used np array, so it does not take time to convert
# to normal array, hence faster
# normal python 0:00:00.028854
# dot function 0:00:00.012048