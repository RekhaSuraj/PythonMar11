# Count the number of characters in a string
str1 = 'Hello World'

# {H:1,e:1,l:3,o:2,r:1,d:1}
char_dict = {}
for i in str1:
	# print(i)
	if i in char_dict:
		char_dict[i] +=1
	else:
		char_dict[i] = 1


print(char_dict)
# {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}


# H 
# char_dict['H'] = 1

# e
# char_dict['e'] = 1


# l
# char_dict['l'] = 1
# char_dict['l'] = char_dict['l'] +1
# char_dict['l'] = 1 + 1
# char_dict['l'] = 2


# o
# char_dict['o'] = 1

# W
# char_dict['W'] = 1 

# o
# char_dict['o'] = char_dict['o'] +1
# char_dict['o'] = 1+1
# char_dict['o'] = 2

# r
# char_dict['r'] = 1

# l
# char_dict['l'] = 2
# char_dict['l'] = char_dict['l'] + 1
# char_dict['l'] = 2 + 1
# char_dict['l'] = 3


# d
# char_dict['d'] = 1


# display only duplicates from the above dictionary

dup_dict = {}
for k in char_dict:
	# print(k)
	if char_dict[k] > 1:
		dup_dict[k] = char_dict[k]

print(dup_dict)
# {'l': 3, 'o': 2}