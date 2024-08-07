# To create a table in MySQL using Python Interface
# To view the structure of table library in MySQL using Python Interface

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",\
                             passwd="prash",database="program")
mycursor=mydb.cursor()
mycursor.execute("create table library (Adm_No int(5) PRIMARY KEY,\
Name varchar(20),Name_of_Book varchar(40),\
Class char(5),Section char(2))")
mycursor.execute("desc library")
for x in mycursor:
    print(x)
