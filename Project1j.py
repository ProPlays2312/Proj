#Updating records dynamically by fetching input from user at run-time

import mysql.connector
mydb = mysql.connector.connect(host="localhost" ,\
                               user="root" ,\
                               password=" ", \
                               database="school")
mycursor = mydb.cursor()
print("Student record Updation")
rno=int(input("Enter rollno to update the record: "))
query="select * from student where Rollno={}".format(rno)
mycursor.execute(query)
myrecord = mycursor.fetchone()
if myrecord != None:
  print("## Record Found- Details are: ##")
  print(myrecord)
  choice=input("Do you want to update marks: (y/n)")
  if choice =='y':
    marks=int(input("Enter new updated marks: "))
    query="UPDATE student set marks = {} where Rollno={}".format(marks, rno)
    mycursor.execute(query)
    mydb.commit()
    print("## Record (s) Updated##")
else:
  print("Sorry! No such student exists")
  mydb.close()