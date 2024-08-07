#CHAPTER 1:REVIEW OF PYTHON
# STRING
#WRITE A PROGRAM TO CHECK WHETHER THE STRING IS PALINDROME OR NOT
str=input('enter a string:')
l=len(str)
p=l-1
index=0
while(index<p):
    if(str[index]==str[p]):
        index=index+1
        p=p-1
    else:
            print('string is not a palindrome')
            break
else:
            print('string is a palindome')
