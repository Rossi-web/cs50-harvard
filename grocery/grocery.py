compras = {

} #Cria uma lista vazia (Dict)

while True: #Pra sempre
    try: #Tente
        item = input().upper().strip() #Pega o input
        if item in compras: #Se o item já estiver na lista, adiciona +1 a quantidade dele
            compras[item] += 1
        else: #Caso contrário, adiciona com valor 1
            compras[item] = 1

    except EOFError: #Caso aperte control D:
        for item in sorted(compras): #Faz x vezes, onde x é a quantidade de itens na lista compras (em ordem alfabética, sorted)
            print(compras[item], item) #Printa primeiro o número(quantidade) e depois o item em si
        break #Para




