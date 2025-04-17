# generate odd numbers from 1 to 20
print(list(filter(lambda x:x%2!=0,range(21))))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Square of odd numbers from above list
print(tuple(map(lambda a:a**2,list(filter(lambda x:x%2!=0,range(21))))))
# (1, 9, 25, 49, 81, 121, 169, 225, 289, 361)

# max of the above numbers
print(max(tuple(map(lambda a:a**2,list(filter(lambda x:x%2!=0,range(21)))))))
# 361

# sum of the squared numbers
print(sum(tuple(map(lambda a:a**2,list(filter(lambda x:x%2!=0,range(21)))))))
# 1330
