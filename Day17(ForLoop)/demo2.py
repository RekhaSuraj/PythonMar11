# Simple calculator program

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

operation = input('Enter an operation')

if operation == '+':
	print('Addition of num1 + num2=',num1+num2)

elif operation == '-':
	print(f'Subtraction of num1 and num2={num1-num2}')

elif operation == '*':
	print(f'Product of num1 and num2={num1*num2}')
else:
	print('Invalid input')


# Enter first number10
# Enter second number5
# Enter an operation+
# Addition of num1 + num2= 15


# Enter first number20
# Enter second number10
# Enter an operation*
# Product of num1 and num2=200


# Enter first number30
# Enter second number5
# Enter an operationsfb
# Invalid input