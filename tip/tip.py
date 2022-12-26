def main():
    dollars = dollars_to_float(input("How much was the meal? ")) #Recebe a informação do valor da refeição
    percent = percent_to_float(input("What percentage would you like to tip? ")) #Recebe a informação da porcentagem da gorjeta
    tip = dollars * percent #Fórmula para cálculo da gorjeta
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    


def percent_to_float(p):
    p = p.replace("%",'')
    p = float (p) / 100
    return float (p) #Tiram o símbolo de % e transformam a porcentagem em um decimal float

main()