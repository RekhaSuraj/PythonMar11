# Tuple methods - Allows only 2 methods
# count() - Return number of occurrences of value
t1 = (11,22,33,44,55,22)
# print(t1.count(22))
# # 2
#
# # No occurrence - Returns 0
# print(t1.count(100))
# 0

# index() - Return first index of value
print(t1.index(22))
# 1

# For fetching index with start and stop
# For more than 1 occurrence, we give start and stop index
print(t1.index(22,2))
# 5


# Syntax Differences
# Feature	        List	                    Tuple
# Declaration	    my_list = [1, 2, 3]	        my_tuple = (1, 2, 3)
# Mutability	    Mutable (Changeable)	    Immutable (Unchangeable)
# Performance	    Slower (More Memory)	    Faster (Less Memory)
# Methods	        More(e.g., append(),
#                   remove())	                Fewer (Only count(), index())
# Use Cases	        When data changes often	    When data remains fixed
