# Nested functions - Function inside another function

def outer_function():
	print('This is outer function')

	def inner_function():
		print('This is inner function')


	print('Before calling inner function')
	inner_function()

print('Before calling outer function')
outer_function()
print('After calling outer function')

# Before calling outer function
# This is outer function
# Before calling inner function
# This is inner function
# After calling outer function