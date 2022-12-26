menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_amount = 0
while True:
    try:
        item = input("Item:").title()
        if item in menu:
            total_amount += menu[item]
            print("Total: $",end="")
            print("{:.2f}".format(total_amount)) # o comando :.2f é usado para que tenham duas casas decimais após a vírgula, assim sendo 29.00, 30.00 etc
    except EOFError:
        print()
        break
