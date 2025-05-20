import csv
# CSV Files - Comma Separated Values
#Python CSV
# A CSV (Comma Separated Values) format is one of the most simple and common ways to store tabular data.
# To represent a CSV file, it must be saved with the .csv file extension.

# Working with CSV files in Python
# While we could use the built-in open() function to work with CSV files in Python, import csv
# there is a dedicated csv module that makes working with CSV files much easier.

with open('emp.csv','w',newline='')as file:
    info1 = csv.writer(file)
    info1.writerow(['EmpId','EmpName','EmpLoc','EmpSalary'])
    while True:
        empId = int(input('Enter Emp Id'))
        empName = input('Enter Emp Name')
        empLoc = input('Enter Emp Location')
        empSal = int(input('Enter Emp Salary'))
        info1.writerow([empId,empName,empLoc,empSal])
        user_input = input('Do you want to insert one more record YES|No?')
        if user_input.lower() == 'no':
            break









