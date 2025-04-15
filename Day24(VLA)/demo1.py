# Variable length Arguments
# 1. Variable-Length Arguments in Python 
# (*args and **kwargs)
# In Python, functions can accept a variable number of arguments using:

# *args → Variable-length positional arguments (Tuple)

# **kwargs → Variable-length keyword arguments (Dictionary)

# 1. Using *args (Multiple/any number Positional Arguments)
# ✅ Allows a function to accept any number of positional arguments.
# ✅ Collects them into a tuple.


def profile(*args):
	print(args)
	for i in args:
		print(i)


print("hello1")

profile(1,2,3,5,'hi','hello',50)
# (1, 2, 3, 5, 'hi', 'hello')

# 1
# 2
# 3
# 5
# hi
# hello