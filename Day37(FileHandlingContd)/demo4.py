with open('demo.txt','r')as file:
    file.seek(10) #Move the cursor to byte 10
    print('cursor point:',file.tell()) #Cursor point should print 10
    print(file.read(5)) #reads 10 characters from the new position - it will print' Python cl'
    print('new cursor point:',file.tell())


#How it works

# file.seek(10) moves the file cursor to the 10th byte
# file.tell() returns the current cursor position.
# file.read(10) reads 10 characters from that position.
# The second file.tell() shows the new position after reading.