# Python program to input names of 'n' countries and their capital and currency , store it in a dictionary and display in tabular form
d1=dict()
i=1
n=int(input("Enter number of entries:"))
while i<=n:
    c=input("Enter country:")
    cap=input("Enter capital:")
    cur=input("Enter currency of country:")
    di[c]=[cap,cur]
    i=i+1
1=d1.keys()
print("\nCountry\t\t","Capital\t\t","Currency")
for i in 1:
    z=d1[i]
    print('\n',i,'\t\t',end=" ")
    for j in z:
    print(j,'\t\t',end="\t\t")
    #searching
x=input("\nEnter Country to be searched: ")
for i in 1:
    if i==x:
        print("\nCountry\t\t","Capital\t\t","Currency\t\t")
        z=d1[i]
        print('\n',i,'\t\t',end="")
      for j in z:
           print(j,'\t\t',end="\t\t")
      break





        
