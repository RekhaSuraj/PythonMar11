# CRUD = C = Create
#        R = Read
       # U = Update
       # D = Delete


import mysql.connector

v1 = mysql.connector.connect(user='root',password='root',host='localhost')

v2 = v1.cursor()

# syntax: create database <database_name>
# v2.execute('create database pencil')
# print('Created',v2)

# Created CMySQLCursor: create database pencil

v2.execute('show databases')
for i in v2:
    print(i)

# ('cap',)
# ('car',)
# ('emp',)
# ('information_schema',)
# ('mango',)
# ('myschema',)
# ('mysql',)
# ('pen',)
# ('pencil',)
# ('performance_schema',)
# ('phone',)
# ('product',)
# ('sys',)