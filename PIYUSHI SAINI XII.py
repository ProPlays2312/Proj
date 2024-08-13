# Queue
#Implementation as a Queue
Library= [ ]
c="y"
while (c=="y"):
    print("1.insert")
    print("2.delete")
    print("3.display")
    choice=int(input("Enter choice:"))
    if (choice==1):
        b=input("Enter book_id:")
        b_name=input("Enter book name:")
        lib=(b,b_name)
        Library.append(lib)
    elif  (choice==2):
        if  (Library==[ ] ):
            print("Queue Empty")
        else:
            print("Deleted element is:",Library.pop(0))
    elif  (choice==3):
        l=len(Library)
        for i in range(0,1):
            print  (Library[ i])
    else:
        print("wrong input")
    c=input("Do you want to continue or not:")
            
        
        
        
        
