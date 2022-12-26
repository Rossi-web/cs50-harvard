def main():
    msg = input()# O texto é inserido pelo usuário
    result = convert(msg) # O resultado é a conversão do texto
    print(result) # Será exibido o texto convertido

def convert(msg):
    msg1 = msg.replace(" ", '...') #Substitue os espaços por ...
    return msg1

main()