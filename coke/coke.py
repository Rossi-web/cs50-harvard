value = int(50) #Preço da coca


for x in range(10): #Realizar o loop por 10 vezes(Mas será interrompido quando a Coca for totalmente paga)
    if value <= 0: #Se o preço já tiver sido totalmente pago, mostra o desconto (se houver) e para o programa
        print("Change owed:", abs(value))
        break;
    else:
        print("Amount due:",value) #Printa o valor que ainda deve ser pago
        coin = int(input("Insert coin: ")) #Valor da moeda inserida
        if coin in [5, 10, 25]: #Compara se as moedas são de 5, 10 ou 25 centavos (sem '' pois é um número?)
            value = (value-coin) #Reduz o valor pago do preço total

print()

