import numpy as np

n = np.array([[1,2,3,4],[5,6,7,8]])
n1 = np.array([[9,10,11,12],[13,14,15,16]])
n3 = np.array([[0,0,0,0],[0,0,0,0]])

print(n)
print()
print(n1)
print()
for i in range(len(n)):
    for j in range(len(n[i])):
        n3[i][j] = n[i][j]+n1[i][j]

print(n3)

# [[10 12 14 16]
#  [18 20 22 24]]
print()
n4 = n+n1
print(n4)
# [[10 12 14 16]
#  [18 20 22 24]]

# hw - Multiplication of n*n1

