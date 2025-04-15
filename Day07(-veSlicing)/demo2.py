# use -1 in step, it returns the reverse string (returns the string from right to left)

v1 = "TODAY IS A GOOD DAY"

print(v1[::-1])
# YAD DOOG A SI YADOT

# # print SI
print(v1[-12:-14:-1])
# SI

# If the start index is greater than stop index, we will get an empty string
print(v1[-12:-14])


# Print 'DOOG' from the above string
print(v1[-5:-9:-1])
# DOOG

print(v1[::-2])
# YDDO  IYDT

# Entire string will be printed as it is if we donot specify any start:stop:step
print(v1[::])
# TODAY IS A GOOD DAY

print(v1[-5:-9:-2])
# DO

quote = 'Python is a high level programming language'


# Assignment
# print 'high level'
# print 'program'
# print 'hgih a si'
# print 'mmargorp'