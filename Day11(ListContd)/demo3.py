# sort and sorted
# sort() - arranges the elements in the original list in ascending order by default
list1 = [90,20,12,45,75,25,34]
list1.sort()
print(list1)
# [12, 20, 25, 34, 45, 75, 90]

# sort or arrange the list in descending order
list1.sort(reverse=True)
print(list1)
# [90, 75, 45, 34, 25, 20, 12]

# sorted() - Return a new list containing all items from the iterable in ascending order
list2 = [30,10,40,20,5,10,65,15]
# print(sorted(list2))
# [5, 10, 10, 15, 20, 30, 40, 65]

list3 = sorted(list2)
print('list3',list3)
# [5, 10, 10, 15, 20, 30, 40, 65]
# list3 [5, 10, 10, 15, 20, 30, 40, 65]
print('list2',list2)
# list2 [30, 10, 40, 20, 5, 10, 65, 15]

# Key Differences:
# Feature	                    sort()	            sorted()
#
# Modifies original list?	    ✅ Yes	            ❌ No
# Returns new list?	            ❌ No	            ✅ Yes
# Works with lists only?	    ✅ Yes	            ❌ No (works with any iterable)
# Memory efficient?	            ✅ Yes	            ❌ No (creates new object)
