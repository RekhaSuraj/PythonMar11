# 'w'       open for writing, truncating(delete/remove) the file first
f2 = open('demo.txt','w')
print(f2)
# <_io.TextIOWrapper name='demo.txt' mode='w' encoding='cp1252'>

f2.write('Good Afternoon Students')
# f2.close()

# If we try to write again in the closed file, we get the below error
# f2.write('GA Again')
# ValueError: I/O operation on closed file.

# To read the parameters
print('Is file closed:',f2.closed)
print('Filename:',f2.name)
print('File Mode:',f2.mode)

# Is file closed: False
# Filename: demo.txt
# File Mode: w

f2.close()
print('Is file closed now:',f2.closed)
# Is file closed now: True
