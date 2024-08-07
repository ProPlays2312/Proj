#To insert a new record into table library in
#MySQL using Python Interface
#Executing SELECT statement using Python

import mysql.connector
mydb=mysql.connector.connect (host="localhost",user="root",\
                             passwd="prash",database="program")
mycursor=mydb.cursor()
mycursor.execute("""INSERT INTO LIBRARY (Adm_No, Name, Name_Of_Book, Class, Section, Book_No)
VALUES (6904, 'Ravi', 'Computer_NCERT', 'VIII', 'B', 2543),
(6994, 'Rahul', 'Science_NCERT', 'VII', 'B', 4671),
(7856, 'Ravi', 'History_NCERT', 'XI', 'E', 8976),
(6124, 'Kunal', 'R.D. Sharma', 'VIII', 'B', 7451),
(9354, 'Rohit', 'Famous Five', 'XI', 'E', 4009),
(9432, 'Atul', 'Python' , 'XII', 'A', 8621)""")
mycursor.execute("select * from library")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)
