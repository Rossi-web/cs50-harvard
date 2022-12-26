import inflect

p=inflect.engine()

itens = []
#Prompt the user for names, one per line
while True:
    try:
        n = input("Input: ")
        itens.append(n)
    #On control-d
    except EOFError:
        if itens == []:
            print()
            pass
        # Add "adieu" to the names with comma and "and" on the end (kkkkk)
        else:
            print()
            break
mylist = p.join(itens)
print("Adieu, adieu, to " + mylist)
