import math

titulo = "Bienvenido al sistema de técnicas de conteo de estadística"
titulo = titulo.center(76, "-")

print("                    ", titulo)
print()

while True:
    try:
        orden = int(input("Digite si importa el orden si(1), no(2): "))

        if orden == 1:

            while True:
                try:
                    utilizan = int(input("Digite si se utilizan todos los elementos si(1) no(2)"))

                    if utilizan == 1:

                        abecedario = "abcdefghijklmnñopqrstuvwxyz"
                        lista_abecedario = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
                        lista_abecedario = lista_abecedario.split(" ")
                        
                        tilde, no_tilde = 'áäéëíïóöúüÁÉËÍÏÓÖÚÜ','aaeeiioouuAEEIIOOUU'
                        conversion = str.maketrans(tilde, no_tilde)

                        print()
                        print("Lo que quiere hallar es una permutacion")
                        print()
                        repeticion = int(input("Digite si hay repetición si(1), no(2): "))

                        if repeticion == 1:

                            while True:
                                try:
                                    print()
                                    print("La fórmula de la permutacion es: PR_n**a, b, c")
                                    print()
                                    palabra = input("Digite la palabra: ")
                                    palabra = palabra.lower()

                                    palabra = palabra.translate(conversion)

                                    cantidad_letras = len(palabra)

                                    lista_repeticion = []
                                    lista_letras = []
                                    
                                    for i in range(0, len(abecedario)):
                                        veces = palabra.count(abecedario[i])
                                        
                                        if veces > 1 or veces == 1:
                                            lista_repeticion.append(veces)
                                            lista_letras.append(abecedario[i])
                                    print()

                                    if not(2 in lista_repeticion):
                                        print("No hay letras repetidas")
                                        print(f"La formula quedaría PR_{cantidad_letras}**1")
                                    
                                    if sum(lista_repeticion)/len(lista_repeticion) != 1:

                                        for i in range(len(lista_repeticion)-1, -1, -1):
                                            if lista_repeticion[i] == 1:
                                                lista_repeticion.remove(lista_repeticion[i])
                                            if palabra.count(lista_letras[i]) == 1:
                                                lista_letras.remove(lista_letras[i])
                                        for i in range(0, len(lista_repeticion)):
                                            print(f"La letra {lista_letras[i]} tiene {lista_repeticion[i]} repeticiones")

                                        print()
                                        print(f"La formula quedaría PR_{cantidad_letras}**", end = "")

                                        for i in range(0, len(lista_repeticion)):
                                            if i != len(lista_repeticion)-1:
                                                print(f"{lista_repeticion[i]}, ", end = "")
                                                
                                            elif i == len(lista_repeticion)-1:
                                                print(f"{lista_repeticion[i]}", end = "")

                                    factorial_denominador = 1

                                    for i in range(0, len(lista_repeticion)):
                                        factorial_denominador *= math.factorial(lista_repeticion[i])
                                    print()

                                    factorial_numerador = math.factorial(cantidad_letras)

                                    resultado = factorial_numerador/factorial_denominador

                                    if resultado % 1 == 0:
                                        resultado = int(resultado)
                                    
                                    if resultado % 1 != 0:
                                        resultado = (f"{resultado:g}")
                                        resultado = float(resultado)

                                    print(f"El resultado de la permutacion es {resultado}")
                                
                                    break
                                except:
                                    print("El valor no es válido")
                        
                        elif repeticion == 2:
                            break
                        else:
                            print("El número no es válido")
                        break
                    elif utilizan == 2:
                        break
                    else:
                        print("El número no es válido")
                except:
                    print("El valor no es válido")
            break
        elif orden ==2:
            print()
            print("Lo que quiere hallar es una combinación")
            print()
            repo = int(input("Digite si la extracción se realiza con reposicion si(1), no(2): "))

            if repo == 1:
                print("La fórmula es C_n,k = n! / (n-k)!k!")
                n = int(input("\nDigite el número de elementos que hay (n): "))
                k = int(input("\nDigite la cantidad de elementos que se utilizan (k): "))
                print(f"La fórmula quedaría C_{n},{k} = {n}! / ({n}-{k})!{k}!")

        else:
            print("El número ingresado no es válido")
    except:
        print("El valor no es válido")