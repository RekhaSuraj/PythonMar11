# Check if a string is a palindrome or not

s1 = input('Enter a string:')
print(s1[::-1])
if s1[::-1] == s1:
	print('String is a Palindrome')
else:
	print('String is Not a Palindrome')


# Enter a string:mom
# String is a Palindrome

# Enter a string:dam
# mad
# String is Not a Palindrome

# Enter a string:dad
# dad
# String is a Palindrome

# Enter a string:level
# level
# String is a Palindrome