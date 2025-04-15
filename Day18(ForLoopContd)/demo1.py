# find the biggest number in a list without using max() inbuilt method

list1 = [40,20,60,30,80,10,100]

big = list1[0] #40
len_list = len(list1)
print(len_list) #6
for i in range(1,len_list):
	if list1[i] > big:
		big = list1[i]
		print('big',big)

print(big)

# 7
# big 60
# big 80
# big 100
# 100

# 7
# big 60
# big 80
# big 100
# 100

# i=1
# 20>40

# i =2
# list1[2] = 60
# 60>40:
# big = 60

# i =3
# list1[3] = 30
# 30>60:

# i=4
# list1[4] = 80
# if 80>60:
# 	big = 80

# i = 5
# list1[5] = 10
# if 10>80:


# Find the smallest number in the list without using min() inbuilt method
list2 = [40,20,60,30,80,10,100]

small = list2[0] #40
len_list = len(list2)
for i in range(1,len_list):
	if list2[i]<small:
		small = list2[i]

print('smallest number is:',small)
# smallest number is: 10



