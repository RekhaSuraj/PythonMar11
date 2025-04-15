# String programs - Write a program to count the words in a sentence
str1 = 'Python is fun and easy'

list1 = str1.split()
print(list1)
# ['Python', 'is', 'fun', 'and', 'easy']
cnt = len(list1)
print(cnt)
# 5

# count number of characters in the above sentence
# print(len(str1))
# 22

cntr = 0
for s in str1:
	cntr += 1


print('cntr',cntr)




