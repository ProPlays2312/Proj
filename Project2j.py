#Menu-driven program to demonstrate four major operations
#performed on a table through MySQL-Python connectivity

def menu():
    c= 'y'
    while (c=='y'):
        print("1. add record")
        print("2. update record")
        print("3. delete record")
        print("4. display records")
        print("5. Exiting")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            adddata()
        elif choice == 2:
            updatedata()
        elif choice == 3:
            deldata()
        elif choice == 4:
            fetchdata()
        elif choice == 5:
            print("Exiting")
            break
        else:
            print("wrong input")
    c = input("Do you want to continue or not?")
def fetchdata():
    import mysql.connector
    try:
        db = mysql.connector.connect(host="localhost", user="root", passwd =" ", database='school')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student")
        results = cursor.fetchall()
        for x in results:
            print(x)
    except:
        print("Error: unable to fetch data")

def adddata():
    import mysql.connector
    db = mysql.connector.connect(host='localhost', user='root', passwd=' ', database='school')
    cursor = db.cursor()
    cursor.execute("INSERT INTO student VALUES ('Ritu', 4000, 'Science', 345, 'B', 11)")
    cursor.execute("INSERT INTO student VALUES ('Ankush', 6000, 'Commerce', 445, 'A', 12)")
    cursor.execute("INSERT INTO student VALUES ('Ajay', 3567, 'Humanities', 446, 'A', 11)")
    cursor.execute("INSERT INTO student VALUES ('Rishav', 8900, 'Science', 545, 'A+', 12)")
    db.commit()
    print("Records added")
def updatedata():
    import mysql.connector
    try:
        db= mysql.connector.connect(host="localhost", user = "root", passwd=' ', database='school')
        cursor = db.cursor()
        sql=("Update student set Marks = 5000 where Name='Rishav'")
        cursor.execute(sql)
        print("Record Updated")
        db.commit()
    except Exception as e:
        print(e)

def deldata():
    import mysql.connector
    db = mysql.connector.connect(host="localhost", user="root", passwd=" ", database="school")
    cursor = db.cursor()
    sql="delete from student where name='Rishav'"
    cursor.execute(sql)
    print("Record Deleted")
    db.commit()

menu()  