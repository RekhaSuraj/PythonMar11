# Default Arguments
# In a function, arguments can have default values.
# We assign default values to the argument using the ‘=’ (assignment) operator at the time of function definition.
# You can define a function with any number of default arguments.


def profile(name1='abc',age=25,salary=50000,company='Google'):
	print(f'Name:{name1}')
	print(f'Age:{age}')
	print(f'Salary:{salary}')
	print(f'Company:{company}')

# without sending any arguments
profile()
print()

# Overriding/replace default arguments
# BY sending arguments
profile('Swaroop')

# overriding name and age
print()
profile('Chethan',27)

# overriding all arguments
print()
profile(name1='Swaroop',age=28, salary=60000,company='Wipro')
