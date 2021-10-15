import math

titulo = "Bienvenido al sistema de técnicas de conteo de estadística"
x = "-"
titulo = titulo.center(76, f"{x}")

print("                    ", titulo)
print()

orden = int(input("Digite si importa el orden si(1), no(2): "))

if orden == 1:

    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    lista_abecedario = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
    lista_abecedario = lista_abecedario.split(" ")
    
    tilde,no_tilde = 'áäéëíïóöúüÁÉËÍÏÓÖÚÜ','aaeeiioouuAEEIIOOUU'
    conversion = str.maketrans(tilde,no_tilde)

    print()
    print("Lo que quiere hallar es una permutacion")
    print()
    repeticion = int(input("Digite si hay repetición si(1), no(2): "))

    if orden == 1:
        print()
        print("La fórmula de la permutacion es: PR_n**a, b, c")
        print()
        palabra = input("Digite la palabra: ")
        palabra = palabra.lower()

        palabra = palabra.translate(conversion)

        cantidad_letras = len(palabra)

        lista_repeticion = []
        lista_letras = []
        
        for i in range(0, len(abecedario)-1):
            veces = palabra.count(abecedario[i])
            
            if veces > 1 or veces == 1:
                lista_repeticion.append(veces)
                lista_letras.append(abecedario[i])
        print()

        print(lista_repeticion)

        if sum(lista_repeticion)/len(lista_repeticion) == 1:
            print("No hay letras repetidas")
            for i in range(0, len(lista_repeticion)):
                print(f"La letra {lista_letras[i]} tiene {lista_repeticion[i]} repeticiones")
                print()
        
        if sum(lista_repeticion)/len(lista_repeticion) != 1:

            for i in lista_repeticion[:]:
                if i == 1:
                    lista_repeticion.remove(i)

            for i in range(0, len(lista_repeticion)):
                print(f"La letra {lista_letras[i]} tiene {lista_repeticion[i]} repeticiones")
        
        print(f"La formula quedaría PR_{cantidad_letras}**", end = "")

        factorial_denominador = 1

        for i in range(0, len(lista_repeticion)):
            if i != len(lista_repeticion)-1:
                print(f"{lista_repeticion[i]}, ", end = "")

            elif i == len(lista_repeticion)-1:
                print(f"{lista_repeticion[i]}", end = "")

            factorial_denominador *= math.factorial(lista_repeticion[i])
        print()

        factorial_numerador = math.factorial(cantidad_letras)

        resultado = factorial_numerador/factorial_denominador

        if resultado % 1 == 0:
            resultado = int(resultado)
        
        if resultado % 1 != 0:
            resultado = (f"{resultado:g}")
            resultado = float(resultado)
        print()

        print(f"El resultado de la permutacion es {resultado}")

