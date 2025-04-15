# control flow statements
# In Python, continue, break, and pass are control flow statements used in loops and 
# conditional statements, but they behave differently:


# 1. break
# Exits the loop completely.

# The execution resumes at the first statement after the loop.


for i in range(10):
	# print(i)
	if i == 3:
		# print(i)
		break

	print(i)


print('After execution of for loop')

# 0
# 1
# 2
# After execution

print('*********')
# 2. continue: It skips the current iteration and goes to the next iteration

for i in range(10):
	if i == 3:
		continue
		print(i)


	print(i)

# 0
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# 9


# pass - Does nothing

for i in range(10):
	if i == 3:
		pass



def function_test():
	pass


class Test:
	...