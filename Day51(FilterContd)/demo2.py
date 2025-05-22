import pandas as pd

df = pd.read_csv('Emp.csv')
print(df)
print()
# print(df.drop_duplicates(subset='Esalary'))

#    Emp_id          Ename  Eage  Esalary Elocation
# 0      11     Ravi kumar    21    34000   chennai
# 1      12   madhavan DOn    23    40000      pune
# 2      13  pramood kumar    27    50000    mumbai
# 3      14         vishal    23    20000     delhi
# 4      15       sireesha    22    30000    kerala
# 5      16  Hareesh kumar    23    45000      Agra
# 8      19       santhosh    22    25000  banglore

print(df.drop_duplicates(subset='Esalary',keep="last"))

#    Emp_id          Ename  Eage  Esalary  Elocation
# 1      12   madhavan DOn    23    40000       pune
# 3      14         vishal    23    20000      delhi
# 5      16  Hareesh kumar    23    45000       Agra
# 6      17          Darla    22    50000     ladakh
# 7      18         Dinesh    23    30000     kerala
# 8      19       santhosh    22    25000   banglore
# 9      20        micheal    25    34000  hyderabad

# Eage

print(df.drop_duplicates(subset="Eage",keep="last"))

#    Emp_id          Ename  Eage  Esalary  Elocation
# 0      11     Ravi kumar    21    34000    chennai
# 2      13  pramood kumar    27    50000     mumbai
# 7      18         Dinesh    23    30000     kerala
# 8      19       santhosh    22    25000   banglore
# 9      20        micheal    25    34000  hyderabad