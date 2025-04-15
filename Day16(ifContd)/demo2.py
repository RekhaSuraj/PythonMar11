# Check for username and pwd from user

un = input('Please enter username')
pwd = int(input('Please enter password'))

if un == 'python' and pwd == 1234:
	print('Access granted')
else:
	print('Access not granted, UN, PWD is wrong')


# Please enter usernamepython
# Please enter password1234
# Access granted

# Please enter usernametest
# Please enter password1234
# Access not granted, UN, PWD is wrong

# Please enter usernamepython
# Please enter password5678
# Access not granted, UN, PWD is wrong