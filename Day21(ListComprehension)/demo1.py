# Statement	Function
# break		Exits the loop entirely
# continue	Skips the current iteration and continues to the next
# pass		Does nothing, acts as a placeholder(for future use)


# while with else - While should not have come out because of break

# In Python, a while loop can have an else clause. The else block executes only if the loop 
# completes normally (i.e., without encountering a break)

# while condition:
#     # Loop body
# else:
#     # Executes if the loop runs to completion (condition becomes False)

# Example 1: while with else (Normal Execution)

# i = 1
# while i <=3:
# 	print(i)
# 	i +=1

# else:
# 	print('Loop completed without a break')


# 1
# 2
# 3 
# Loop completed without a break

i = 1
while i <=3:
	if i == 2:
		print('breaking at i=',i)
		break

	print(i)
	i +=1

else:
	print('Loop completed without a break')


# 1
# breaking at i= 2







