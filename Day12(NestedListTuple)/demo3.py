v1 = [20,40,50,60,[[70,80,90],100,'python'],'welcome',85,[100,200],300]
# -ve indexing

print('value at index -1:',v1[-1])
print('value at index -2:',v1[-2])
print('value at index -3:',v1[-3])
print('value at index -4:',v1[-4])
print('value at index -5:',v1[-5])
print('value at index -6:',v1[-6])
print('value at index -7:',v1[-7])
print('value at index -8:',v1[-8])
print('value at index -9:',v1[-9])

# value at index -1: 300
# value at index -2: [100, 200]
# value at index -3: 85
# value at index -4: welcome
# value at index -5: [[70, 80, 90], 100, 'python']
# value at index -6: 60
# value at index -7: 50
# value at index -8: 40
# value at index -9: 20

# print 90 using -ve indexing
print(v1[-5][-3])
# [70, 80, 90]

print(v1[-5][-3][-1])
# 90

