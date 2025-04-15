# globals()
#     Return the dictionary containing the current scope's global variables.

#     NOTE: Updates to this dictionary *will* affect name lookups in the current
#     global scope and vice-versa.

# Using the same variable for local and global scope
var = 100

def profile():
	var = 200
	sum_n = 0
	print(var)
	print(globals()['var'])
	sum_n = var + globals()['var']
	return sum_n


s = profile()
print(s)
# 200
# 100
# 300
# print(help(globals))

# Updated the global varaible 
v = 10
def greet():
	v = 20
	globals()['v'] = 30

print('Before',v)
greet()
print('After',v)

# Before 10
# After 30