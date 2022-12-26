import random

while True:
    #Prompt the user for n
    try:
        l = int(input("Level: "))
        #If its not a positive integer, reprompt
        if l>0:
            #Generate a number between 1 and n (random module)
            break
    except:
        pass

r = random.randint(1.0, l)

while True:
    #Prompt the user to guess an integer (if != integer, reprompt)
    try:
        g = int(input("Guess: "))
        #If the number is too small, print Too small! and reprompt
        if g < r:
            print("Too small!")
        #If the number is too large, print Too large! and reprompt
        elif g > r:
            print("Too large!")
        #If the number is right, print Just right! and exit
        else:
            print("Just Right!")
            break
    except:
        pass