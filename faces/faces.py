def main():
    msg = input()# O texto é inserido pelo usuário
    result = convert(msg) # O resultado é a conversão do texto
    print(result) # Será exibido o texto convertido

def convert(msg):
    msg1 = msg.replace(":)", '🙂') #Converte as carinhas felizes
    msg2 = msg1.replace(":(", '🙁') #Converte as carinhas tristes EM ADICIONAIS as felizes, como mostrado na msg1
    return msg2

main()