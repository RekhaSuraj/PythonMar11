import pandas as pd

df = pd.read_csv('emp.csv')
print(df)

#    EmpId  EmpAge   EmpName EmpLoc  EmpSalary
# 0      1      20   Swaroop    Blr     100000
# 1      2      21   Chethan     AP     100000
# 2      3      22  Surendra     UK     100000
# 3      4      23    Seetha    IND     200000
# 4      5      24     Shiva     US     300000

print()
print(df.rename(columns={'EmpLoc':'EmpLocation'}))
# print()
print(df)
# changes will not be applied to the original df
#    EmpId  EmpAge   EmpName EmpLoc  EmpSalary
# 0      1      20   Swaroop    Blr     100000
# 1      2      21   Chethan     AP     100000
# 2      3      22  Surendra     UK     100000
# 3      4      23    Seetha    IND     200000
# 4      5      24     Shiva     US     300000


# inplace = True to apply changes permanently
df.rename(columns={'EmpLoc':'EmpLocation','EmpAge':'EmployeeAge'},inplace=True)
print(df)

#    EmpId  EmployeeAge   EmpName EmpLocation  EmpSalary
# 0      1           20   Swaroop         Blr     100000
# 1      2           21   Chethan          AP     100000
# 2      3           22  Surendra          UK     100000
# 3      4           23    Seetha         IND     200000
# 4      5           24     Shiva          US     300000