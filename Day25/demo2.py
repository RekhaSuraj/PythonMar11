# How to take local variable outside - making it global

def function_test():
    v = 10

# print(v)
# NameError: name 'v' is not defined
# function_test()

# syntax: global <variable_name> - A local variable can be conveted to global
def profile():
    global v
    v = 20

# print('before calling:',v)
# NameError: name 'v' is not defined
profile()
print('global v from local-outside function:',v)
# global v from local 20