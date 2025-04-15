# isnumeric() - Return True if the string is a numeric string, False otherwise.
# isdigit() returns True if all characters in the string are digits (0-9), and False otherwise.
# It also considers exponents like '²' as digits.
# isnumeric() returns True if all characters in the string are numeric characters,
# including digits, fractions, subscripts, superscripts, Roman numerals, and currency numerators.

str1 = "12345"
print(str1.isnumeric())
# True

print(str1.isdigit())
# True

string3 = "½"
print('NUmeric',string3.isnumeric())
print('digit',string3.isdigit())
# NUmeric True
# digit False

string2 = "12²"
print('Numeric',string2.isnumeric())
print('digit',string2.isdigit())
# Numeric True
# digit True


string4 = "IV"
print('Numeric',string4.isnumeric())
print('digit',string4.isdigit())
# Numeric False
# digit False


