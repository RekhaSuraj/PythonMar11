# Write a program to reverse a number using while loop

# 1234 % 10
# 4321

num = int(input('Enter a number'))
rev_num = 0
while num != 0:
	rem = num % 10 # extra
	rev_num = (rev_num * 10) + rem # append rem to rev_num
	num = num // 10 # remove the last digit from num

print(rev_num)
# Enter a number1234
# 5432

# Enter a number1230
# 321

# 1234  ----> 5432

# 4 --> 10)1234(123
#          1230
#          -----
#             4


# 3 --> 10)123(12
#          120
#         -------
#           3


# 2 --> 10)12(1
#          10
#         -------
#           2


# 1 --> 10)1(0
#          0
#         -------
#           1






