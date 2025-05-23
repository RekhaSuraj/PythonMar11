import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost',database='pencil')

v2 = v1.cursor()

# To create Table
# Cmysql : create table Table_Name(col1 datatype, col2 datatype ,...........)

# v2.execute('create table student(Sno int,Firstname varchar(20), Age int, Address varchar(30))')
# print(v2)

# CMySQLCursor: create table student(Sno int,Firstname v..

v2.execute('desc student')

print(v2)
# CMySQLCursor: desc student

for i in v2:
    print(i)


# ('Sno', 'int', 'YES', '', None, '')
# ('Firstname', 'varchar(20)', 'YES', '', None, '')
# ('Age', 'int', 'YES', '', None, '')
# ('Address', 'varchar(30)', 'YES', '', None, '')

# Index	Field Name	Meaning
# 0	    Field	Column name (e.g., 'Fname')
# 1	    Type	Data type (e.g., b'varchar(30)')
# 2	    Null	Whether NULL values are allowed ('YES' or 'NO')
# 3	    Key	Key type ('PRI' for primary, 'MUL' for index, etc.)
# 4	    Default	Default value (e.g., None means no default)
# 5	    Extra	Extra info (e.g., 'auto_increment')


# v2.close()