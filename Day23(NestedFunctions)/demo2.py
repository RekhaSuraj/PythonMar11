# Outer function parameters are accessible inside inner function also (Closures)
def greet(name1):

	def message():
		return f'hello {name1}'


	return message()


var = greet('GRK Students')
print(var)

# hello GRK Students