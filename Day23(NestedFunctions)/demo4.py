# Arguments
# Types of Arguments:
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable length arguments

# Positional arguments:
# Positional arguments are those arguments where values get assigned to the arguments by their 
# position when the function is called.
# For example, the 1st positional argument must be 1st when the function is called.
# The 2nd positional argument needs to be 2nd when the function is called, etc

def profile(name1,age,salary):
	print(f'Name:{name1}')
	print(f'Age:{age}')
	print(f'Salary:{salary}')


profile('Swaroop',25,50000)
# Name:Swaroop
# Age:25
# Salary:50000

profile(25,50000,'Swaroop')
# Name:25
# Age:50000
# Salary:Swaroop

