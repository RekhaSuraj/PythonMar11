# Scope of variables

# Understanding Scope
# In programming, the scope of a name defines the area of a program in which you can unambiguously access 
# that name, such as variables, functions, objects, and so on. 
# A name will only be visible to and accessible by the code in its scope.
# Several programming languages take advantage of scope for avoiding name collisions and unpredictable behaviors. 


# There are four type's scopes
# 1.Local scope
# 2.Global scope
# 3.Enclosing scope(Nested function / closures)
# 4.Built-in Scope


# What is local variable/local scope ? 
# A local variable is variable , which is defined inside the function, we access within the function

def greet():
	b = 20
	print('Inside the function',b)


greet()
# Inside the function 20

# print(b)
# NameError: name 'b' is not defined

