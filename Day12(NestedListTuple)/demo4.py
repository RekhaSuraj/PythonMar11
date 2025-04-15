s1 = [11,22,33,44,[['a','b','c'],'d',55],66,77,[88,[99,100]],200]
# print ['a','b','c'] using slicing
# list[start:stop:step]

print(s1[0:5])
# [11, 22, 33, 44, [['a', 'b', 'c'], 'd', 55]]

print(s1[4:5])
# [[['a', 'b', 'c'], 'd', 55]]
print(s1[4:5][0])

# ['a', 'b', 'c'] - using indexing
print(s1[4][0])

# using slicing
print(s1[4][0:1])
# [['a', 'b', 'c']]

print(s1[4][0][1:2])
# ['b']

# assignment
l2 = [1,2,['a',2,[3],5,6],[3,'d','r','t','d',[[11,22,33],[12,13,14],[34,56,78],11,12,13],'abc'],'python','java']

# print 12 - first 12 using indexing and slicing

# print 22 - using indexing and slicing

# [2,[3],5,6] using slicing
