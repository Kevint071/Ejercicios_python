titulo = "LISTA DE ESTUDIANTES"
titulo = ("{:>42}".format(titulo))
print(titulo, "\n")

asteriscos_head = ("*" * 10) +("                                        ") + ("  " + "*" * 23)

print(asteriscos_head)

code = "CÓDIGO"
name = "NOMBRE ESTUDIANTE"

code = ("{:>8}".format(code))
print(code, end = "")

name = ("{:>64}".format(name))
print(name)
print(asteriscos_head)

nombres = {
    1: "Jose Cardenas",
    2: "Luis Manchego",
    3: "Diego Monzon",
    4: "Diana Gimenez",
    5: "Carolina Guzman"
}

temas = {
    1: "Nombre",
    2: "Apellido",
    3: "Sexo",
    4: "Código"
}

jose = {
    1: "Jose",
    2: "Cardenas",
    3: "Masculino",
    4: "E001"
}

luis = {
    1: "Luis",
    2: "Manchego",
    3: "Masculino",
    4: "E002"
}

diego = {
    1: "Diego",
    2: "Monzon",
    3: "Masculino",
    4: "E003"
}

diana = {
    1: "Diana",
    2: "Gimenez",
    3: "Femenino",
    4: "E004"
}

carolina = {
    1: "Carolina",
    2: "Guzman",
    3: "Femenino",
    4: "E005"
}

lista = []

lista.append(jose[2])
lista.append(luis[2])
lista.append(diego[2])
lista.append(diana[2])
lista.append(carolina[2])

def agregar_personas ():
    lista_nueva = []

    for i in range(0, len(lista)):
        lista_nueva.append(lista[i][0])
def E00i (i):
    print(f"   E00{i}                                              {nombres[i]}")
E00i(1)
E00i(2)
E00i(3)
E00i(4)
E00i(5)
print(asteriscos_head)

print("\nEn la siguiente lista elija un número: \n")
print("1. Mostrar un alumno")
print("2. Mostrar todo el contenido")
print("3. Mostrar solo códigos")
print("4. Mostrar solo datos")
print("5. Mostrar solo varones")
print("6. Mostrar solo damas\n")

lista_inicial = int(input("Digite un número de esta lista: "))

if lista_inicial == 1:
    code = input("Digite un código: ")
    code = code[-1]
    code = int(code)

    if code == 1:
        print()
        for i in enumerate(jose):
            print(temas[i[1]], ":", jose[i[1]])
    if code == 2:
        print()
        for i in enumerate(luis):
            print(temas[i[1]], ":", luis[i[1]])
    if code == 3:
        print()
        for i in enumerate(diego):
            print(temas[i[1]], ":", diego[i[1]])
    if code == 4:
        print()
        for i in enumerate(diana):
            print(temas[i[1]], ":", diana[i[1]])
    if code == 5:
        print()
        for i in enumerate(carolina):
            print(temas[i[1]], ":", carolina[i[1]])

elif lista_inicial == 2:

    print("\nDigite si quiere:\n")
    print("1. Contenido Estándar")
    print("2. Ordenado por Apellidos")
    print("3. Ordenado por Número de Matrícula")

    num_orden = int(input("\nDigite alguno de los números de la lista: "))

    if num_orden == 1:
        print("\nINFORMACIÓN DE JOSE CARDENAS\n")
        for i in enumerate(jose):
            print(temas[i[1]], ":", jose[i[1]])

        print("\nINFORMACIÓN DE LUIS MANCHEGO\n")
        for i in enumerate(luis):
            print(temas[i[1]], ":", luis[i[1]])

        print("\nINFORMACIÓN DE DIEGO MONZON\n")
        for i in enumerate(diego):
            print(temas[i[1]], ":", diego[i[1]])

        print("\nINFORMACIÓN DE DIANA GIMENEZ\n")
        for i in enumerate(diana):
            print(temas[i[1]], ":", diana[i[1]])
        
        print("\nINFORMACIÓN DE CAROLINA GUZMAN\n")
        for i in enumerate(carolina):
            print(temas[i[1]], ":", carolina[i[1]])
    
    elif num_orden == 2 or num_orden == 3:
        print("\nINFORMACIÓN DE JOSE CARDENAS\n")
        for i in enumerate(jose):
            print(temas[i[1]], ":", jose[i[1]])

        print("\nINFORMACIÓN DE DIANA GIMENEZ\n")
        for i in enumerate(diana):
            print(temas[i[1]], ":", diana[i[1]])
        
        print("\nINFORMACIÓN DE CAROLINA GUZMAN\n")
        for i in enumerate(carolina):
            print(temas[i[1]], ":", carolina[i[1]])
        
        print("\nINFORMACIÓN DE LUIS MANCHEGO\n")
        for i in enumerate(luis):
            print(temas[i[1]], ":", luis[i[1]])
        
        print("\nINFORMACIÓN DE DIEGO MONZON\n")
        for i in enumerate(diego):
            print(temas[i[1]], ":", diego[i[1]])

elif lista_inicial == 3:
    print("\nCÓDIGO DE JOSE CARDENAS\n")
    print(temas[4], ":", jose[4])

    print("\nCÓDIGO DE DIANA GIMENEZ\n")
    print(temas[4], ":", diana[4])
        
    print("\nCÓDIGO DE CAROLINA GUZMAN\n")
    print(temas[4], ":", carolina[4])
        
    print("\nCÓDIGO DE LUIS MANCHEGO\n")
    print(temas[4], ":", luis[4])
        
    print("\nCÓDIGO DE DIEGO MONZON\n")
    print(temas[4], ":", diego[4])

elif lista_inicial == 4:
    print("\nDATOS DE JOSE CARDENAS\n")
    print(temas[1], ":", jose[1])

    print("\nDATOS DE LUIS MANCHEGO\n")
    print(temas[1], ":", luis[1])
        
    print("\nDATOS DE DIEGO MONZON\n")
    print(temas[1], ":", diego[1])
        
    print("\nDATOS DE DIANA GIMENEZ\n")
    print(temas[1], ":", diana[1])
        
    print("\nDATOS DE CAROLINA GUZMAN\n")
    print(temas[1], ":", carolina[1])

elif lista_inicial == 5:
    print("\nINFORMACIÓN DE JOSE CARDENAS\n")
    for i in enumerate(jose):
        print(temas[i[1]], ":", jose[i[1]])
    
    print("\nINFORMACIÓN DE LUIS MANCHEGO\n")
    for i in enumerate(luis):
        print(temas[i[1]], ":", luis[i[1]])
    
    print("\nINFORMACIÓN DE DIEGO MONZON\n")
    for i in enumerate(diego):
        print(temas[i[1]], ":", diego[i[1]])

elif lista_inicial == 6:
    print("\nINFORMACIÓN DE DIANA GIMENEZ\n")
    for i in enumerate(diana):
        print(temas[i[1]], ":", diana[i[1]])
    
    print("\nINFORMACIÓN DE CAROLINA GUZMAN\n")
    for i in enumerate(carolina):
        print(temas[i[1]], ":", carolina[i[1]])
