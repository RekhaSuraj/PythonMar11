# Indexing - A unique number for every element(letter) in the string
# Indexing starts from 0 to n-1

str1 = 'HELLO WORLD'

# len() - Returns the total number of elements in the string
# Syntax : len(string)
print(len(str1))
# 11

# Positive Indexing
print('value at index 0:',str1[0]) # H
print('value at index 1:',str1[1]) # E
print('value at index 2:',str1[2]) # L
print('value at index 3:',str1[3]) # L
print('value at index 4:',str1[4]) # O
print('value at index 5:',str1[5]) # 
print('value at index 6:',str1[6]) # W
print('value at index 7:',str1[7]) # O
print('value at index 8:',str1[8]) # R
print('value at index 9:',str1[9]) # L
print('value at index 10:',str1[10]) # D

# value at index 0: H
# value at index 1: E
# value at index 2: L
# value at index 3: L
# value at index 4: O
# value at index 5:  
# value at index 6: W
# value at index 7: O
# value at index 8: R
# value at index 9: L
# value at index 10: D

# print('value at index 11:',str1[11])

# IndexError: string index out of range

str2 = 'Welcome to Python'

# Print the letter P
print(str2[11])
# P

print(str2[8])
# t

print(str2[13])
# t

