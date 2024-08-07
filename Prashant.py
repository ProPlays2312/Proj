# To create a new database 'program' from python to mysql
# To check for all the databases present in MYSQL using Python
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="prash")
mycursor=mydb.cursor()
mycursor.execute("create database program")
mycursor.execute("show databases;")
for x in mycursor:
    print(x)
    

