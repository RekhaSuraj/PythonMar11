# r		Read the data in this file
# read() : Returns the entire file content and it accepts the optional size parameter
# that mentions the bytes to read from the file.
# read file using the with


with open('demo.txt','r') as file:
    print(file.read())

# Good Afternoon Students
# Welcome to Python class
# Welcome to SQL Class
# Welcome to Django class
print(file.closed)
# True

f1 = open('demo.txt','r')
print(f1.read())
# Good Afternoon Students
# Welcome to Python class
# Welcome to SQL Class
# Welcome to Django class
print(f1.closed)
# False