# create an empty function
def empty_function():
	pass

# call
empty_function()


# Take parameters - Number of arguments passed should be same as number of parameters defined
# def parameter_function(param1,param2,param3......):
# 	# body of function

# parameter_function(Arg1,Arg2,Arg3....)

def take_parameters(n1,n2):
	print('addition',n1+n2)


# take_parameters()
# TypeError: take_parameters() missing 2 required positional arguments: 'n1' and 'n2'

# take_parameters(5)
# TypeError: take_parameters() missing 1 required positional argument: 'n2'

take_parameters(5,6)
# addition 11

take_parameters(10,20)
# addition 30

take_parameters(30,35)
# addition 65


# take_parameters(1,2,3)
# TypeError: take_parameters() takes 2 positional arguments but 3 were given