v1 = [20,40,50,60,[[70,80,90],100,'python'],'welcome',85,[100,200],300]

print(len(v1))
# 9
print('value at index 0:',v1[0])
print('value at index 1:',v1[1])
print('value at index 2:',v1[2])
print('value at index 3:',v1[3])
print('value at index 4:',v1[4])
print('value at index 5:',v1[5])
print('value at index 6:',v1[6])
print('value at index 7:',v1[7])
print('value at index 8:',v1[8])

print(v1[4])
# [[70, 80, 90], 100, 'python']
print(v1[4][0])
# [70, 80, 90]

print(v1[4][0][2])
# 90
