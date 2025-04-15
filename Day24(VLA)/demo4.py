# Global scope
# A global variable is variable , which is defined outside the function,
# we access it anywhere in or outside of the function.


x = 100
print('Global variable outside the function',x)
def profile():
	y = 200
	print('Local variable inside the function',y)

print('Global var called outside the function 2',x)
profile()
print('Global var called outside the function 3',x)

# Global variable outside the function 100
# Global var called outside the function 2 100
# Local variable inside the function 200
# Global var called outside the function 3 100