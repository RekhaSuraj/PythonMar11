# Simple ATM Program

balance = 1000
amount = int(input('Enter the amount to be withdrawn'))

if amount < balance:
	print('Transaction successful')
	balance = balance - amount
	print('Your new balance is:',balance)
else:
	print('Insufficient balance')


# Enter the amount to be withdrawn2000
# Insufficient balance

# Enter the amount to be withdrawn250
# Transaction successful
# Your new balance is: 750

# Validate for username and password check