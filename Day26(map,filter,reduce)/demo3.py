# Print names that start with 'a' or 'A'
list1 = ['Ajay','Amar','Joy','Tim','atul']

def start_with_A(word):
    if word[0].lower() == 'a':
        return word

print(list(filter(start_with_A,list1)))
# ['Ajay', 'Amar', 'atul']

# using lambda
print(list(filter(lambda w:w[0].lower()=='a',list1)))
# ['Ajay', 'Amar', 'atul']

# startswith() - hw

