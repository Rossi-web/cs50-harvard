mes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#Pede o prompt do usuário em um formato MM/DD/YYYY
while True:
    data = input("date: ")
    try:
        if "," in data:
            data = data.replace(",","")
            m, d, y = data.split()
            new_d = int(d)
            new_y = int(y)
            for i in range(len(mes)):
                if m == mes[i]:
                    new_m = i+1
            #Confere se o mês está na lista 'mes' e se possui menos de 31 dias e é entre 1 e 12 (caso seja número)
            if (new_d <= 31 and new_d >= 1) and (new_m >= 1 and new_m <= 12):
                #Printa a data convertida em formato YYYY-MM-DD
                print(f"{new_y}-{new_m:02}-{new_d:02}")
                break
            else:
                pass
        else:
            raise ValueError
    except ValueError:
        try:
            m, d, y = data.split("/")
            new_m = int(m)
            new_d = int(d)
            new_y = int(y)
            #Confere se o mês está na lista 'mes' e se possui menos de 31 dias e é entre 1 e 12 (caso seja número)
            if (new_d <= 31 and new_d >= 1) and (new_m >= 1 and new_m <= 12):
                #Printa a data convertida em formato YYYY-MM-DD
                print(f"{new_y}-{new_m:02}-{new_d:02}")
                break
            else:
                pass

        except ValueError:
            pass


