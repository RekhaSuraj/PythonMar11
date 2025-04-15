# For Loop
# Looping statements - For loop
# In Python, the for loop is used to iterate over a sequence such as a list, string, tuple, 
# other iterable objects such as range.
#
# With the help of for loop, we can iterate over each item present in the sequence and 
# execute the same set of operations for each item.
# Using a for loops in Python we can automate and repeat tasks in an efficient manner.
#
# So the bottom line is using the for loop we can repeat the block of statements a fixed number 
# of times.
# for loop :
# Iterables : list,string,tuple,set,dict,range,array

# default start value is 0
# range(start=num,stop=num,step=1)
# x = range(1,11)
# print(type(x))
# <class 'range'>

# syntax : for var in iterable:
#               body of for loop

# For loop for a list
list1 = [10,20,30,40,50,50]


for var in list1:
	print(var)

# 10
# 20
# 30
# 40
# 50
# 50

# If we want to print items next to each other, we use end=' '
print()
for v in list1:
	print(v,end=' ')

print()