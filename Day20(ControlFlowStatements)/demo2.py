# Write a program to check if a number is prime or not from user

num = int(input('Enter a number'))
is_prime = True
for i in range(2,num):
	if num % i == 0:
		print(f'{num} is not a prime')
		is_prime = False
		break

	else:
		# print(f'{num} is a prime')
		is_prime = True


# Enter a number4
# 4 is not a prime

# Enter a number5
# 5 is a prime
# 5 is a prime
# 5 is a prime

if is_prime == False:
	print('Not a prime number')
else:
	print('Prime number')


# Enter a number5
# Prime number

# Enter a number6
# Not a prime number