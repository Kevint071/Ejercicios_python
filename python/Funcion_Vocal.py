while True:
    caracter = input("Digite un solo carácter: ")

    if len(caracter) > 1:
        print("Solamente puede digitar un carácter\n")
    else:
        break

lista_vocales = ["a", "e", "i", "o", "u"]

if caracter in lista_vocales:
    print("True")
else:
    print("False")