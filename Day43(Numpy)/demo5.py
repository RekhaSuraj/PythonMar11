# Creating One-Dimensional Array by using UserInput:
import numpy as np
# What is ndarray ?
# In numpy, we can hold data by using array Data structure.
# The array which are created by using numpy are called ndarray
# ndarray --> N-Dimensional Array or NUmpy array
# This ndarray mostly used in DataScience libraries like pandas, scipy etc

array_list = int(input('Enter the size :'))
a1 = np.ndarray(shape=[array_list], dtype=int)
print('Enter elements :', array_list)
for i in range(array_list):
    a1[i] = int(input('Enter element'))

print('Array elements :',a1)
# Array elements : [1 2 3 4 5 6]