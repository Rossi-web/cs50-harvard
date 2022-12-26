from pyfiglet import Figlet
import random
import sys
#Expects zero or two command line arguments

figlet = Figlet()

#Zero if the user would like to output in a random font
if len(sys.argv)== 1:
    isRandomFont = True
#Two if specific font, first = -f or --font, and the second with the name of the font
elif len(sys.argv)==3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    print("Invalid Usage")
    sys.exit(1)

#Prompt the user for a str of text
figlet.getFonts()

#Output the text in the desired font
if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid Usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

text = input("Input: ")

print("Output: ")
print(figlet.renderText(text))