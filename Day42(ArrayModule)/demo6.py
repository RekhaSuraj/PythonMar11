import array
import sys

d1 = array.array('d',[1,2,3,4,5])
print(d1)
# array('d', [1.0, 2.0, 3.0, 4.0, 5.0])

print(d1[3])
# 4.0

print('Itemsize:',d1.itemsize)
# 8

print('Memorysize:',sys.getsizeof(d1))
# Memorysize: 120

# | Feature             | Signed Integer             | Unsigned Integer                    |
# | ------------------- | -------------------------- | ----------------------------------- |
# | Supports negatives  | ✅ Yes                      | ❌ No                              |
# | Value range (8-bit) | -128 to +127               | 0 to 255                            |
# | Storage size        | Same (e.g., 1 byte)        | Same                                |
# | Use cases           | Temperatures, gains/losses | Memory addresses, sizes, RGB values |
#
# Think of an 8-bit unsigned int like a ruler with 256 units (0 to 255),
# and a signed int like a ruler centered at 0, ranging from -128 to 127.
