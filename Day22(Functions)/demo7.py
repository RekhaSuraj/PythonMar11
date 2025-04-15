# Factorial of a number using function

def fact_num(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact*i

	return fact


res = fact_num(int(input('Enter a number')))
print('Factorial',res)

# Enter a number4
# Factorial 24

print(fact_num(5))
# 120
