# Write a program to find out sum until user enters 0 using while loop

# 5
# 10
# 2
# 0

# total - 17

num = int(input('Enter a number'))
sum1 = 0
while num != 0:
	sum1 = sum1 + num
	print('sum1',sum1)
	num = int(input('Enter another number'))

print(sum1)

# Enter a number5
# sum1 5
# Enter another number10
# sum1 15
# Enter another number2
# sum1 17
# Enter another number0
# 17



