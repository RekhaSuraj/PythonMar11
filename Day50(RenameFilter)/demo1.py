import csv

with open('emp.csv','w',newline='')as file:
    info1 = csv.writer(file)
    info1.writerow(['EmpId','EmpAge','EmpName','EmpLoc','EmpSalary'])
    while True:
        empId = int(input('Enter Emp Id'))
        empAge = int(input('Enter Emp Age'))
        empName = input('Enter Emp Name')
        empLoc = input('Enter Emp Location')
        empSal = int(input('Enter Emp Salary'))
        info1.writerow([empId,empAge,empName,empLoc,empSal])
        user_input = input('Do you want to insert one more record YES|No?')
        if user_input.lower() == 'no':
            break
