# Print Prime number or not using functions
def Prime_Num(num):
	is_prime = True
	for i in range(2,num):
		if num%i == 0:
			is_prime = False
			break

	return is_prime


var = Prime_Num(7) 
print(var)
# True

# var1 = Prime_Num(8) 
# print(var1)
# # False

if var == True:
	print('Prime Number')
else:
	print('Not a prime Number')