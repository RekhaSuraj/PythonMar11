# Nested if 

# Nested if-else statement
# In Python, the nested if-else statement is an if statement inside another if-else statement. 
# It is allowed in Python to put any number of if statements in another if statement.
#
# Indentation is the only way to differentiate the level of nesting. 
# The nested if-else is useful when we want to make a series of decisions.
#
# Syntax of the nested-if-else:
#
# if conditon_outer:
#     if condition_inner:
#         statement of inner if
#     else:
#         statement of inner else:
#     
# else:
#     Outer else
# statement outside if block

# Check for even odd 
num = int(input('Enter a number:'))

if num > 0:
	if num % 2 == 0:
		print('Even number')
	else:
		print('Odd number')
else:
	print('Invalid input')


# Enter a number:8
# Even number

# Enter a number:7
# Odd number

# Enter a number:0
# Invalid input

# Enter a number:-8
# Invalid input