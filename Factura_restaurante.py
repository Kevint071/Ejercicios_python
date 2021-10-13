import datetime

# Se imrpime la lista

titulo = "LISTA DE PRECIOS"
titulo = ("{:>32}".format(titulo))
print(titulo)

asteriscos_head = ("*" * 10) + ("  " + "*" * 23) + ("  " + "*" * 10)

print(asteriscos_head)

code = "CÓDIGO"
des = "DESCRIPCIÓN"
price = "PRECIO"

code = ("{:>8}".format(code))
print(code, end = "")

des = ("{:>21}".format(des))
print(des, end = "")

price = ("{:>16}".format(price))
print(price)

print(asteriscos_head)

def P00i (i):
    print(f"   P00{i}     ", end = "")
P00i(1)
print("Arroz con pollo" + "          /S.  18.00")

P00i(2)
print("Loeno saltado" + "            /S.  22.00")

P00i(3)
print("Arroz con mariscos" + "       /S.  25.00")

P00i(4)
print("Jalea pescado" + "            /S.  29.00")

P00i(5)
print("Ceviche" + "                  /S.  24.00")

P00i(6)
print("Parihuela" + "                /S.  27.00")

P00i(7)
print("Pollo al cilindro" + "        /S.  30.00")

print(asteriscos_head)

# Se comienzan a pedir datos sobre la factura

lista_comidas = []
lista_precio = []
lista_cantidad = []
lista_codigo = []

while True:
    while True:
        codigo = input("Digite el codigo de lo que quiere comer: ")
        
        if codigo == "P001" or codigo == "p001":
            codigo1 = "P001"
            comida1 = "Arroz con pollo"
            lista_comidas.append(comida1)
            price1 = 18
            lista_precio.append(price1)
            while True:
                try:
                    cantidad1 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad1)
                    lista_codigo.append(codigo1)
                    break
                except:
                    print()
                    print("El número no es válido")
            break
            
        elif codigo == "P002" or codigo == "p002":
            codigo2 = "P002"
            comida2 = "Loeno saltado"
            lista_comidas.append(comida2)
            price2 = 22
            lista_precio.append(price2)
            while True:
                try:
                    cantidad2 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad2)
                    lista_codigo.append(codigo2)
                    break
                except:
                    print()
                    print("El número no es válido")
            break
            
        elif codigo == "P003" or codigo == "p003":
            codigo3 = "P003"
            comida3 = "Arroz con mariscos"
            lista_comidas.append(comida3)
            price3 = 25
            lista_precio.append(price3)
            while True:
                try:
                    cantidad3 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad3)
                    lista_codigo.append(codigo3)
                    break
                except:
                    print()
                    print("El número no es válido")
            break
            
        elif codigo == "P004" or codigo == "p004":
            codigo4 = "P004"
            comida4 = "Jalea Pescado"
            lista_comidas.append(comida4)
            price4 = 29
            lista_precio.append(price4)
            while True:
                try:
                    cantidad4 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad4)
                    lista_codigo.append(codigo4)
                    break
                except:
                    print()
                    print("El número no es válido")
            break

        elif codigo == "P005" or codigo == "p005":
            codigo5 = "P005"
            comida5 = "Ceviche"
            lista_comidas.append(comida5)
            price5 = 24
            lista_precio.append(price5)
            while True:
                try:
                    cantidad5 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad5)
                    lista_codigo.append(codigo5)
                    break
                except:
                    print()
                    print("El número no es válido")
            break

        elif codigo == "P006" or codigo == "p006":
            codigo6 = "P006"
            comida6 = "Parihuela"
            lista_comidas.append(comida6)
            price6 = 27
            lista_precio.append(price6)
            while True:
                try:
                    cantidad6 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad6)
                    lista_codigo.append(codigo6)
                    break
                except:
                    print()
                    print("El número no es válido")
            break
            
        elif codigo == "P007" or codigo == "p007":
            codigo7 = "P007"
            comida7 = "Pollo al cilindro"
            lista_comidas.append(comida7)
            price7 = 30
            lista_precio.append(price7)
            while True:
                try:
                    cantidad7 = int(input("Digite la cantidad de platos que va a ordenar de este tipo: "))
                    lista_cantidad.append(cantidad7)
                    lista_codigo.append(codigo7)
                    break
                except:
                    print()
                    print("El número no es válido")
            break
        
        else:
            print("El codigo escrito no es válido")
            print()
    
    while True:
        otra_orden = input("¿Desea ordenar otra comida? si/no: ")

        if otra_orden == "si" or otra_orden == "no":
            break

        if otra_orden != "si" and otra_orden != "no":
            print()
            print("La palabra ingresada no es válida")

    if otra_orden == "no":
        break

name = input("Digite su nombre: ")
name = name.upper()
direccion = input("Digite su dirección: ")
direccion = direccion.upper()
ruc = input("Digite la RUC N° de la tienda: ")
ruc = ruc.upper()
lista_subtotal = []

for i in range(0, len(lista_comidas)):
    pago_total = lista_precio[i] * lista_cantidad[i]
    lista_subtotal.append(pago_total)

total_a_pagar = sum(lista_subtotal) + 21.96
total_a_pagar = (f"{total_a_pagar:g}")

if float(total_a_pagar) % 1 == 0:
    total_a_pagar = int(total_a_pagar)
        
if float(total_a_pagar) % 1 != 0:
    total_a_pagar = float(total_a_pagar)

print(f"El total a pagar es de /S. {total_a_pagar}")
while True:
    try:
        paga_usuario = float(input("Digite el valor con que va a pagar: "))
        
        if paga_usuario % 1 == 0:
            paga_usuario = int(paga_usuario)
        
        if paga_usuario % 1 != 0:
            paga_usuario = float(paga_usuario)
        
        if paga_usuario < total_a_pagar:
            print("El pago es insuficiente")
        
        if paga_usuario >= total_a_pagar:
            print()
            print()
            break
    except:
        print()
        print("El valor debe ser un número")
    
cambio = paga_usuario - total_a_pagar
    
fecha_actual = datetime.datetime.now()
fecha_actual = fecha_actual.strftime("%d/%m/%Y")
    
cambio = (f"  S/.  {cambio:.2f}")

# Ahora se procede a imprimir la factura

nombre = "NOMBRE"
fecha = "FECHA"
direccion_n = "DIRECCIÓN"
ruc_n = "RUC N°"
cambio_n = "T-CAMBIO"
cantidad_n = "CANTIDAD"
price = "PRECIO S/."
subtotal_n = "SUBTOTAL"

print(nombre, end = "")

print(name.center(60, " "), end = "")

print(f"{fecha}: {fecha_actual}")

print(direccion_n, end = "")

print(direccion.center(54, " "), end = "")

print(f"   {ruc_n}: {ruc}")

print(cambio_n.rjust(74, " "), end = "")

print(f":  {cambio}")

print(code, end = "")

des = ("{:>28}".format(des))
print(des, end = "")

cantidad_n = ("{:>28}".format(cantidad_n))

print(cantidad_n, end = "")

price = ("{:>13}".format(price))

print(price, end = "")

subtotal_n = ("{:>11}".format(subtotal_n))

print(subtotal_n)

for i in range(len(lista_comidas)):
    print(lista_codigo[i].center(9, " "), end = "")
    print(" " * 16, end = "")
    print(lista_comidas[i].ljust(31, " "), end = "")
    print(str(lista_cantidad[i]).center(8, " "), end = "")
    print("   ", end = "")
    print(f"S/.  {lista_precio[i]:.2f}", end = "")
    print("  ", end = "")
    print(str(f"S/.  {lista_subtotal[i]:.2f}").center(10, " "))

print()
print()
print()
total_sin_igv = total_a_pagar - 21.96
total_a_pagar_n = (f"TOTAL A PAGAR S/.     S/.  {total_sin_igv:.2f}")
print(total_a_pagar_n.rjust(81, " "))
igv_n = (f"Igv 18%      S/.  21.96")
print(igv_n.rjust(81, " "))
total_a_pagar = total_a_pagar + 21.96
total_a_pagar_n = (f"TOTAL A PAGAR $      S/.  {total_a_pagar:.2f}")
print(total_a_pagar_n.rjust(82, " "))

salida = input("Presione enter para salir")