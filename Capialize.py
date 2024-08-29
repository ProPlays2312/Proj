#Function to capitalize the first letter of a sentence. def capitalize_sentence():
def capitalize_sentence():
    f1 = open("C:\\Users\\user\\Desktop\\4.txt","r")
    f2 = open("C:\\Users\\user\\Desktop\\5'.txt", "w")
    while 1:
        line = f1.readline()  #Read a line
        if not line:
            break    #Encounter EOF

        # Stripe off the new-line character and any whitespace on the right
        line = line.rstrip()
        lineLength = len(line)
        str= ""   #String to concatenate all character from line
        str = str + line [0].upper()
        i = 1
        # Loop to check a line to convert uppercase
        while i < lineLength:
            if line[i] == ".":
                str=str + line[i]
                i = i+1
                if i >= lineLength:
                    break
                str = str + line[i].upper()
            else:
                str = str + line[i]
            i=i+1
        f2.write(str)
    else:
        print("Source file does not exist")
    f1.close()
    f2.close()

capitalize_sentence()
        
