# Replace negative numbers with 0 using list comprehension
nums = [10,20,30,-40,5,-60,-80]

n1 = [i if i>0 else 0 for i in nums]
print(n1)
# [10, 20, 30, 0, 5, 0, 0]