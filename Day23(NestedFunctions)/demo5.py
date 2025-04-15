# Keyword Arguments
# Arguments are passed by parameter names, so order does not matter.


def profile(name1,age,salary,company):
	print(f'Name:{name1}')
	print(f'Age:{age}')
	print(f'Salary:{salary}')
	print(f'Company:{company}')


profile(name1='Surendra',age=25,salary=50000,company='Google')
profile(age=25,name1='Chethan',company='Google',salary=50000)

print('***************')
# Mixing positional and keyword arguments - 
# First you should provide positional arguments and then keyword arguments

profile('Swaroop',company='Microsoft',age=25,salary=60000)
print('***************')

# profile('Swaroop',company='TCS',60000,age=25)
# SyntaxError: positional argument follows keyword argument