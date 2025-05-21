# Filter rows based on condition
import pandas as pd

df = pd.read_csv('Emp1.csv')
print(df)

print()
# Fetch single column
# print(df['Ename'])

# Fetch records whose salary > 30000
# sal = df['Esalary']> 30000
# print(sal)

print(df[df['Esalary']> 30000])

#    Emp_id          Ename  Eage  Esalary  Elocation
# 0      11     Ravi kumar    21    34000    chennai
# 1      12   madhavan DOn    23    40000       pune
# 2      13  pramood kumar    27    50000     mumbai
# 5      16  Hareesh kumar    23    45000       Agra
# 6      17          Darla    22    50000     ladakh
# 9      20        micheal    25    34000  hyderabad

# &(ampersand) - and operator symbol

# print(df[(df['Esalary']>30000) & (df['Esalary']<50000)])


#    Emp_id          Ename  Eage  Esalary  Elocation
# 0      11     Ravi kumar    21    34000    chennai
# 1      12   madhavan DOn    23    40000       pune
# 5      16  Hareesh kumar    23    45000       Agra
# 9      20        micheal    25    34000  hyderabad

print()
# | (pipe symbol) - or operator
print(df[(df['Esalary']>40000) | (df['Eage']>22)])

#    Emp_id          Ename  Eage  Esalary  Elocation
# 1      12   madhavan DOn    23    40000       pune
# 2      13  pramood kumar    27    50000     mumbai
# 3      14         vishal    23    20000      delhi
# 5      16  Hareesh kumar    23    45000       Agra
# 6      17          Darla    22    50000     ladakh
# 7      18         Dinesh    23    30000     kerala
# 9      20        micheal    25    34000  hyderabad

# ^ - Exor
# ~ - Not
# hw - Print records where Elocation is not 'chennai'

