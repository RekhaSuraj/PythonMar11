# Even and odd numbers from 0 to 10

for i in range(11):
	if i % 2 == 0:
		print('even',i)

	else:
		print('odd',i)


# even 0
# odd 1
# even 2
# odd 3
# even 4
# odd 5
# even 6
# odd 7
# even 8
# odd 9
# even 10

# Even and odd numbers in separate lists

even_list = []
odd_list = []
for j in range(11):
	if j %2 == 0:
		even_list.append(j)

	else:
		odd_list.append(j)


print('even list',even_list)
print('odd list',odd_list)

# even list [0, 2, 4, 6, 8, 10]
# odd list [1, 3, 5, 7, 9]