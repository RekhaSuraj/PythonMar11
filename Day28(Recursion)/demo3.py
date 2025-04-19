# 3 components of a recursive function
# 1. Function Definition
# 2. Base case (Exit Case)
# 3. Recursive Case

# Print numbers in reverse order using recursion
def print_nos(x): # Function Definition
    if x <= 0: #Exit Case (Base Case)
        print('End')

    else:
        print(x)
        x=x-1
        print_nos(x) # Recursive case

print_nos(5)
# 5
# 4
# 3
# 2
# 1
# End



