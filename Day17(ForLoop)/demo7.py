# Print +ve and -ve numbers in 2 separate lists
list1 = [10,20,-40,-10,50,-60,70,-100]

pos_list = []
neg_list = []
for l in list1:
	if l > 0:
		pos_list.append(l)

	else:
		neg_list.append(l)

print('Positive List',pos_list)
print('Negative List',neg_list)

# Positive List [10, 20, 50, 70]
# Negative List [-40, -10, -60, -100]

