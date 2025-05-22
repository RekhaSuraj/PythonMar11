import pandas as pd

df = pd.read_csv('Emp.csv')
print(df)
#    Emp_id          Ename  Eage  Esalary  Elocation
# 0      11     Ravi kumar    21    34000    chennai
# 1      12   madhavan DOn    23    40000       pune
# 2      13  pramood kumar    27    50000     mumbai
# 3      14         vishal    23    20000      delhi
# 4      15       sireesha    22    30000     kerala
# 5      16  Hareesh kumar    23    45000       Agra
# 6      17          Darla    22    50000     ladakh
# 7      18         Dinesh    23    30000     kerala
# 8      19       santhosh    22    25000   banglore
# 9      20        micheal    25    34000  hyderabad

print()
# print(df.duplicated(subset='Esalary'))

# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6     True
# 7     True
# 8    False
# 9     True
# dtype: bool

# print()
# print(df.loc[df.duplicated(subset='Esalary')])

#    Emp_id    Ename  Eage  Esalary  Elocation
# 6      17    Darla    22    50000     ladakh
# 7      18   Dinesh    23    30000     kerala
# 9      20  micheal    25    34000  hyderabad


# keep (optional):
# 'first' (default): Mark duplicates except the first occurrence as True.
# 'last': Mark duplicates except the last occurrence as True.
# False: Mark all duplicates as True.
# A Boolean Series where True indicates a duplicate row.

# print()
# print(df.duplicated(subset='Esalary',keep="last"))

# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# 5    False
# 6    False
# 7    False
# 8    False
# 9    False
# dtype: bool

print()

# print(df.loc[df.duplicated(subset='Esalary',keep="last")])

#    Emp_id          Ename  Eage  Esalary Elocation
# 0      11     Ravi kumar    21    34000   chennai
# 2      13  pramood kumar    27    50000    mumbai
# 4      15       sireesha    22    30000    kerala

# Eage

print(df.loc[df.duplicated(subset='Eage')])

#    Emp_id          Ename  Eage  Esalary Elocation
# 3      14         vishal    23    20000     delhi
# 5      16  Hareesh kumar    23    45000      Agra
# 6      17          Darla    22    50000    ladakh
# 7      18         Dinesh    23    30000    kerala
# 8      19       santhosh    22    25000  banglore

# hw - keep="last" for Eage