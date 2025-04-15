l1 = [10,-20,-30,50,60,-70,-90,100]

# neg_list = []
# pos_list = []
# for i in l1:
# 	if i < 0:
# 		neg_list.append(i)
# 	else:
# 		pos_list.append(i)


# print(neg_list)
# [-20, -30, -70, -90]

# using list comprehension
list1 = [j for j in l1 if j<0]

print('list comprehension',list1)
# list comprehension [-20, -30, -70, -90]

list2 = [k for k in l1 if k >0]
print('pos_numbers',list2)
# pos_numbers [10, 50, 60, 100]

