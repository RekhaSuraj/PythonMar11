# readline()	The readline() method reads a single line from a file at a time. .
# Accepts optional size parameter that mentions how many bytes to return from the file.

# Read single line
# with open('demo.txt','r') as file:
#     print(file.readline())

# print 2 lines
# with open('demo.txt','r')as file:
#     print(file.readline(),end='')
#     print(file.readline())

# Printed 3 lines
# with open('demo.txt','r')as file:
#     for i in range(1,4):
#         print(file.readline(),end='')


# using for loop without readline
with open('demo.txt','r')as file:
    for line in file:
        print(line,end="")