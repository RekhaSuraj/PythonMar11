# range()

# range(start, stop, step)
# start (optional) – The starting number (default is 0).
# stop – The sequence stops before this number (mandatory).
# step (optional) – The increment between numbers (default is 1).

for var in range(0,10):
	print(var)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# printing even numbers using step count 2
print()
for var in range(0,11,2):
	print(var)

# 0
# 2
# 4
# 6
# 8
# 10

# Printing in reverse order
print()
for var in range(10,0,-1):
	print(var)


# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

