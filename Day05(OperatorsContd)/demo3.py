# Bitwise operator - Works on binaries (bits). There are 6 bitwise operators
# Bitwise & (and)- ampersand
# Bitwise | (or) - Pipe
# Bitwise ^ (XOR) - cap
# Bitwise not ~ (Tilde) 
# Bitwise shiftleft (<<)
# Bitwise shiftright (>>)

# Bitwise and (&) - Performs and operation on binaries.

a = 5
b = 4
print(a&b)
# 4

# 5 --> 0  1  0  1
# 4 --> 0  1  0  0
# & --------------
#       0  1  0  0 --->4

x = 6
y = 7
print(x&y)
# 6

# 6 --> 0  1  1  0
# 4 --> 0  1  0  0
# & --------------
#       0  1  1  0 --->6

l = 0b101
b = 0b100

print(l&b)
# 4

# Bitwise or (|) operator = performs or operation on binaries
x = 8
y = 9
print(x | y)
# 9

print(10 | 12)
# 14
