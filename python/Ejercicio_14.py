import datetime
print("Digite las fechas (dd/mm/aaaa) y separe los datos con (/)")

while True:
    try:
        print("Digite la fecha 1")

        fecha_1 = input()

        fecha_1 = fecha_1.split("/")

        fecha_1[0] = int(fecha_1[0])
        fecha_1[1] = int(fecha_1[1])
        fecha_1[2] = int(fecha_1[2])

        fecha_1 = datetime.date(fecha_1[2], fecha_1[1], fecha_1[0])

        break

    except:
        print("La fecha no es válida")

while True:
    try:        
        print("Digite la fecha 2")
        
        fecha_2 = input()
        
        fecha_2 = fecha_2.split("/")
        
        fecha_2[0] = int(fecha_2[0])
        fecha_2[1] = int(fecha_2[1])
        fecha_2[2] = int(fecha_2[2])
        
        fecha_2 = datetime.date(fecha_2[2], fecha_2[1], fecha_2[0])
        
        dias = fecha_2 - fecha_1

        dias = dias.days

        dias = abs(dias)

        print("La diferencia entre las dos fechas es de {} dias".format(dias))

        break

    except:
        print("La fecha no es válida")
