# Print first 7 numbers which are divisible by 7 and 8 using while loop


cntr = 0
n = 0
while cntr <= 7:
	if n % 7 == 0 and n % 8 == 0:
		print(n)
		cntr = cntr + 1

	n = n+1

# 0
# 56
# 112
# 168
# 224
# 280
# 336
# 392

