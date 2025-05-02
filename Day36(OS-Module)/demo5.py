#  'a'       open for writing, appending to the end of the file if it exists

f1 = open('demo.txt','a')
print(f1)
c1 = f1.write('\nWelcome to Python class')
c2 = f1.write('\nWelcome to SQL Class')
c3 = f1.write('\nWelcome to Django class')

print(c1,c2,c3)
# Number of characters in the string
# 24 21 24
f1.close()

# f1.write('Hello')
# ValueError: I/O operation on closed file.