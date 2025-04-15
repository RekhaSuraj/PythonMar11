#print even numbers from 1 to 10 using list comprehension
# even_list = []
# for i in range(11):
# 	if i % 2 == 0:
# 		even_list.append(i)

# print(even_list)
# [0, 2, 4, 6, 8, 10]


e_list = [i for i in range(11) if i%2 == 0]
print(e_list)
# [0, 2, 4, 6, 8, 10]


# odd numbers

o_list = [j for j in range(11) if j%2 !=0]
print(o_list)
# [1, 3, 5, 7, 9]