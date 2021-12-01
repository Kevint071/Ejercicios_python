lista_letras = []

def es_palindromo(palabra):
    for i in palabra:
        lista_letras.append(i)

    lista_letras_inversa = reversed(lista_letras)

    palabra1 = "".join(lista_letras)
    palabra2 = "".join(lista_letras_inversa)

    if palabra1 == palabra2:
        print("Las palabras es palíndroma")
    else:
        print("La palabra no es palíndroma")
        
es_palindromo(input("Ingrese una palabra: "))