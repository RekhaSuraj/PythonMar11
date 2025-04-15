# if elif else condition
#Chain multiple if statement in Python
# In Python, the if-elif-else condition statement has an elif blocks to chain 
# multiple conditions one after another. This is useful when you need to check multiple conditions.
#
# With the help of if-elif-else we can make a tricky decision. The elif statement checks 
# multiple conditions one by one and if the condition fulfills, then executes that code.
#
# Syntax of the if-elif-else statement:
#
# if condition-1:
#      statement 1
# elif condition-2:
#      stetement 2
# elif condition-3:
#      stetement 3
#      ...
# else:
#      statement

# In the above example, the elif conditions are applied after the if condition.
# Python will evalute the if condition and if it evaluates to False then it will evalute
# the elif blocks and execute the elif block whose expression evaluates to True.
# If multiple elif conditions become True, then the first elif block will be executed.


num1 = int(input('Enter a number'))
if num1 == 1:
	print('Sunday')
elif num1 == 2:
	print('Monday')
elif num1 == 3:
	print('Tuesday')
elif num1 == 4:
	print('Wednesday')
elif num1 == 5:
	print('Thursday')
elif num1 == 6:
	print('Friday')
elif num1 == 7:
	print('Saturday')
else:
	print('Invalid input')

# Enter a number0
# Invalid input

# Enter a number7
# Saturday