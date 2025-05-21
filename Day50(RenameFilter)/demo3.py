import pandas as pd
# rename(override) all the column names

df = pd.read_csv('emp.csv')
print(df)

#    EmpId  EmpAge   EmpName EmpLoc  EmpSalary
# 0      1      20   Swaroop    Blr     100000
# 1      2      21   Chethan     AP     100000
# 2      3      22  Surendra     UK     100000
# 3      4      23    Seetha    IND     200000
# 4      5      24     Shiva     US     300000



print()
new_cols = ['Emp_Id','Emp_Age','Emp_Name','Emp_Loc','Emp_Sal']
df.columns = new_cols
print(df)

#    Emp_Id  Emp_Age  Emp_Name Emp_Loc  Emp_Sal
# 0       1       20   Swaroop     Blr   100000
# 1       2       21   Chethan      AP   100000
# 2       3       22  Surendra      UK   100000
# 3       4       23    Seetha     IND   200000
# 4       5       24     Shiva      US   300000
