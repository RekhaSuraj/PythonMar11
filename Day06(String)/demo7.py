# Slicing - Fetching part of a string
# Syntax : start:stop:step
# start - From which (where) index to start. Default value is 0
# stop - Till where index to fetch + 1. Default value is n-1
# step - Jumps, Default value is 1

quote = 'Knowledge is Power'
print(len(quote))
# 18

# print 'is'
print(quote[10:12])
# is

# By giving start index
# print 'Know'
print(quote[0:4])
# Know

# Without giving start index, it starts from 0
print(quote[:4])
# Know

# Giving start and stop index
# print 'Power'
print(quote[13:18])
# Power

# Without giving stop index, default value is n-1
print(quote[13:])
# Power

print(quote[:5:1])
# Knowl

quote = 'Knowledge is Power'
print(quote[0:10:2])
# Kolde

print(quote[::1])
# Knowledge is Power

print(quote[::2])
# Koldei oe

