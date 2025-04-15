str1 = 'Today is Wednesday'

# print(help(str))

# casefold() - Return a version of the string suitable for caseless comparisons
# casfold() - Converts the sting lowercase
# lower() is simpler and only converts ASCII characters to lowercase. It is suitable for basic string comparisons when dealing with English text or when case sensitivity is not a major concern.
# casefold() is more aggressive and handles a wider range of Unicode characters,
# including special characters and accented letters. It is recommended for more
# robust case-insensitive string comparisons, especially when working with multilingual text.
print(str1.casefold())

string2 = "ß is German"
print('casefold',string2.casefold())
# casefold ss is german

print('lower',string2.lower())
# lower ß is german

# startswith('letter/item') - Returns True if a string starts with the specified character
# Return True if S starts with the specified prefix, False otherwise.
print(str1.startswith('T'))
# True

print(str1.startswith('Q'))
# False

print(str1.startswith('T',1))
# False

print(str1.startswith('i',1))
# False


# endswith(letter/item) - Return True if S ends with the specified suffix, False otherwise
# Returns True if a string ends with the specified character
print(str1.endswith('y'))
# True

print(str1.endswith('x'))
# False
