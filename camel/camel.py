camel = input("camelCase: ")# Pede pelo input em camelCase

print("snake_case: ",end="") # Printa o resultado em snake_case

for letter in camel:
    if letter.isupper(): #Se a letra for maiúscula
        print("_" + letter.lower(), end="") # coloca um _ antes da letra em minúsculo
    else:
        print(letter, end="") # Caso não seja maiúscula, apenas continua printando normalmente

print()
