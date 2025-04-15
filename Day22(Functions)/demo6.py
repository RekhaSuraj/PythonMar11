# Return from a function - return

# Return Value From a Function
# In Python, to return value from the function, a return statement is used. 
# It returns the value of the expression following the returns keyword.

# Syntax of return statement

# def fun():
#     statement-1
#     statement-2
#     statement-3
#     .          
#     .          
# 	return [expression]
# The return value is nothing but a outcome of function.

# The return statement ends the function execution.
# For a function, it is not mandatory/compulsory to return a value.
# If a return statement is used without any expression, then the None is returned.
# The return statement should be inside of the function block.

def greet():
	return 'Good Morning All'


var = greet()
print(var)
# Good Morning All

print(greet())
# Good Morning All