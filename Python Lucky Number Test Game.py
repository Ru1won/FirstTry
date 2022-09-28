y = (True)
x = float(input("what is the lucky number?"))
while (y == True):
    if x < 6:
        print ("too low")
        x = float(input("what is the lucky number?"))
    elif x > 6:
        print ("too high")
        x = float(input("what is the lucky number?"))
    elif x == 6:
        print ("CORRECT")
        y = False
    else:
        ()

