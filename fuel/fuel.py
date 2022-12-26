#While forever
while True:
    #Get user input
    fuel = input("Fraction: ")
    try:
        #Try to split the fuel
        x, y = fuel.split("/")
        #Convert into integers
        new_x = int(x)
        new_y = int(y)
        #Calculate the percentage
        f = new_x / new_y
        #Check if its less than one and then stop the loop
        if f<=1:
            break

    except(ValueError, ZeroDivisionError):
        pass
#Multiply Percentage by 100
p = int(round(f * 100))
#Check if percentage is less than 1, print E
if p<=1:
    print("E")
#Check if percentage is more than 99, print F
elif p>=99:
    print("F")
else:
    print(f"{p}%")
