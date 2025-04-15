# Pattern printing
# Square pattern

for i in range(5):
	for j in range(5):
		print(j,end=" ")

	print()

# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 


print('------'*5)
for i in range(5):
	for j in range(5):
		print('*',end=" ")

	print()

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# Print a rectangle pattern
print('------'*5)
for i in range(5):
	for j in range(3):
		print('*',end=" ")

	print()

# * * * 
# * * * 
# * * * 
# * * * 
# * * *


print('------'*5)
# Print a right angled triangle
for i in range(1, 5):
	for j in range(i):
		print('*',end=" ")

	print()

# * 
# * * 
# * * * 
# * * * * 