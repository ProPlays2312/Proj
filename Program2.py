# To input elements in a tuple and pass it to a function to determine the total
#number of even and odd numbers in it.
def countEvenodd(tup):
    counteven = 0
    countodd = 0
    for i in tup:
        if i%2 == 0:
            counteven += 1
        else:
            countodd += 1
    return counteven, countodd
tup1 = ()
n = int(input("Enter the total elements in a tuple: "))
for i in range(n):
    num = int(input("Enter the number :"))
    tup1 = tup1 + (num,)
count_stats = countEvenodd(tup1)
print("Even numbers are:", count_stats[0])
print("odd numbers are:", count_stats[1])
