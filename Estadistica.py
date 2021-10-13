titulo = "Bienvenido al sistema de técnicas de conteo de estadística"
x = "-"
titulo = titulo.center(76, f"{x}")

print("                    ", titulo)

orden = int(input("Digite si importa el orden si(1), no(2): "))

abecedario = "abcdefghijklmnñopqrstuvwxyz"
lista_abecedario = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
lista_abecedario = lista_abecedario.split(" ")

a,b = 'áäéëíïóöúüÁÉËÍÏÓÖÚÜ','aaeeiioouuAEEIIOOUU'
trans = str.maketrans(a,b)

if orden == 1:
    print()
    print("Lo que quiere hallar es una permutacion")
    repeticion = int(input("Digite si hay repetición si(1), no(2): "))
    if orden == 1:
        print()
        print("La fórmula de la permutacion es: PR_n**a, b, c")
        palabra = input("Digite la palabra: ")
        palabra = palabra.lower()

        palabra = palabra.translate(trans)

        print(palabra)

        lista_repeticion = []
        lista_letras = []
        
        for i in range(0, len(abecedario)-1):
            veces = palabra.count(abecedario[i])
            
            if palabra.count(abecedario[i]) > 1:
                lista_repeticion.append(veces)
                lista_letras.append(abecedario[i])

        print(lista_repeticion)
        print(lista_letras)