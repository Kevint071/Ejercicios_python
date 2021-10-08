import datetime

# x = datetime.datetime.now()

# print(x)

# x = x.strftime("Son las %H horas")

# print(x)

# x = datetime.date(2021, 12, 12)

# x = x.strftime("%Y/%m/%d")

# print(x)

fecha_actual = datetime.datetime.now()

y = input("Digite su fecha de nacimiento: ")

lista = y.split("/")

lista[2] = int(lista[2])
lista[1] = int(lista[1])
lista[0] = int(lista[0])

print(lista)

fecha_nacimiento = datetime.date(lista[2], lista[1], lista[0])

fecha_nacimiento = fecha_nacimiento.strftime("%d/%m/%Y")

fecha_nacimiento = datetime.date(fecha_nacimiento)

print(fecha_nacimiento)

fecha_total = fecha_actual - fecha_nacimiento

print(fecha_total)
