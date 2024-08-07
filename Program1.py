# Program to simulate a traffic light comprising of
#two user defined functions trafficlight() and light().

def trafficlight():
    signal = input("Enter the colour of the traffic light: ")
    if(signal not in ("RED", "YELLOW", "GREEN")):
        print("Please enter a valid Traffic Light colour in CAPITALS")
    else:
        value = light(signal) #function call to light()
        if (value == 0):
            print("STOP, Life is more important than speed")
        elif (value == 1):
            print("Please Go SLOW")
        else:
            print("You may go now")
def light(color):
    if(color == "RED"):
        return (0)
    elif(color == "YELLOW"):
        return (1)
    else:
        return (2)
# function ends here
trafficlight()
print("BETTER LATE THAN NEVER")
