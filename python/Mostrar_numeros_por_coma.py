num = input("Escriba varios números separados por coma: ")

num = num.split(",")
lista_num = []

for i in num:
    i = i.strip(" ")
    
    if float(i) % 1 == 0:
        i = int(i)
    else:
        i = float(i)

    lista_num.append(i)

print(lista_num)
