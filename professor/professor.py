import random



def main():
    level = get_level()
    tentativas = 0
    pontuacao = 0
    for _ in range(10):
        int(x)
        int(z)
        generate_integer(n)
        resposta = input (x "+" y "=")
        z = x+y
        if tentativas < 3:
            if resposta = (z):
                pontuacao = pontuacao + 1
            else:
                print("EEE")
                tentativas = tentativas + 1
        else:
            print(z)

def get_level():
    n = input("Level")
    int(n)

def generate_integer(n):
    try:
        if n=1:
            x = random.randrange(10)
            y = random.randrange(10)
        elif n=2:
            x = random.randrange(10, 100)
            y = random.randrange(10, 100)
        elif n=3:
            x = random.randrange(100, 1000)
            y = random.randrange(100, 1000)
        else:
            raise ValueError
    except ValueError:
        pass



if __name__ == "__main__":
    main()