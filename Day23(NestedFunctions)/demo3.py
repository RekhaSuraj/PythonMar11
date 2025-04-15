# Sum of numbers from outer and inner functions
def sum_outer(n1,n2,n3):
	sum1 = n1+n2+n3

	def sum_inner(a,b,c):
		sum2 = a+b+c
		return sum2


	var = sum1+sum_inner(10,20,30)
	return var

res = sum_outer(1,2,3)
print('sum of variables from outer and inner functions:',res)

# sum of variables from outer and inner functions: 66


