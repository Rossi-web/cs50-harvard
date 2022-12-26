conta = input("Digite o cálculo: ")

x,y,z = conta.split(" ")

x2 = float(x)
z2 = float(z)

if y=="+":
    print(x2+z2)
elif y=="-":
    print(x2-z2)
elif y=="*" or y=="x" or y=="X":
    print(x2*z2)
else:
    print(x2/z2)