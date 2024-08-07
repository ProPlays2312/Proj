#To modify table library (adding a new column) in
#MySQL using Python Interface
# To view the modified structure  of table student in
#MySQL using Python Interface 

import mysql.connector
mydb=mysql.connector.connect (host="localhost",user="root",\
                             passwd="prash",database="program")
mycursor=mydb.cursor()
mycursor.execute ("alter table library add(Book_No int (4))")
mycursor.execute ("desc library")

for x in mycursor:
    print(x)
