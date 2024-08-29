# Menu driven program to input names of n students, total marks, average and result

n=int(input("No of students:"))
tup=[ ]
names=[ ]
for i in range (n):
    name=input("Name:")
    t_marks=int(input("Total marks:"))
    avg=float(input("Average:"))
    t=(name,t_marks,avg)
    tup+=(t, )
while True:
    print("MENU")
    print("1 . Accept")
    print("2 . Display")
    print("3 . Search")
    print("4 . Merit list")
    print("5 . Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        for i in tup:
            print(i[0] , "-" , i[2])
            if i[2]>32:
                print("Result : Pass")
            else:
                print("Result : Fail")
    elif ch==2:
                print("Name\tTotal Marks\tAverage")
        for i in tup: 
                print(i[0] , i[1] , "\t" , i[2])
    elif ch==3:
                name1=input("Name:")
                if name1 in names:
                            print("Name\tTotal Marks\tAverage")
                            pos=names.index(name1)
                            print(tup[pos] [0] , tup[pos] [1] , tup[pos] [2])
                else:
                            print("Name not found")
    elif ch==4:
                print("MERIT LIST")
                for i in tup:
                    if i[2]>74
                            print(i[0])
     elif ch==5:
                break
     else:
                print("Invalid Choice")
