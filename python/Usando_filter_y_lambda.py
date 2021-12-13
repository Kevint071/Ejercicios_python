abecedario = "abcdefghijklmnñopqrstuvwxyz"
lista_abecedario = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
lista_abecedario = lista_abecedario.split(" ")

tilde, no_tilde = 'áäéëíïóöúüÁÉËÍÏÓÖÚÜ','aaeeiioouuAEEIIOOUU'
conversion = str.maketrans(tilde, no_tilde)

palabra = input("Digite la palabra: ")
palabra = palabra.lower()
#Aquí ya se utiliza la conversión de la palabra quitando las tildes a la palabra digitada
palabra = palabra.translate(conversion)
cantidad_letras = len(palabra)

lista_repeticion = []
lista_letras = []
                                        
#Este ciclo sirve para añadir las veces que se repite una letra en la palabra digitada a la lista llamada lista_repeticion y además añade la letra que se repitió a una lista llamada lista_letras
for i in abecedario:
    veces = palabra.count(i)
                                            
    if veces > 1 or veces == 1:
        lista_repeticion.append(veces)
        lista_letras.append(i)
print()
if not 2 in lista_repeticion:
    print("No hay letras repetidas")
    print(f"La formula quedaría PR = {cantidad_letras}!")
                                        
elif sum(lista_repeticion)/len(lista_repeticion) != 1:
        
    lista_repeticion = list(filter(lambda x: True if x > 1 else False, lista_repeticion))
    lista_letras = list(filter(lambda x: True if palabra.count(x) > 1 else False, lista_letras))
    print(lista_repeticion)
    print(lista_letras)
                                                    
    for i in range(0, len(lista_repeticion)):
        print(f"La letra {lista_letras[i]} tiene {lista_repeticion[i]} repeticiones")

    print(f"\nLa formula quedaría PR = {cantidad_letras}! / ", end = "")

    for i in range(0, len(lista_repeticion)):
        if i != len(lista_repeticion)-1:
            print(f"{lista_repeticion[i]}! x", end = " ")
        else:
            print(f"{lista_repeticion[i]}!", end = "")