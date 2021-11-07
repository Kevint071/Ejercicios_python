lista = []

def valor_lista ():
    while True:
        try:
            valores = float(input("Digite el valor de su lista: "))
            if valores % 1 == 0:
                valores = int(valores)
            if valores % 1 != 0:
                valores = (f"{valores:g}")
                valores = float(valores)
            lista.append(valores)
            while True:
                yn = input("¿Desea digitar otro número? y/n: ")
                print()
                if yn != "y" and yn != "Y" and yn != "n" and yn != "N":
                    print("El valor especificado no es válido")
                if yn == "y" or yn == "Y" or yn == "n" or yn == "N":
                    break
            if yn == "n" or yn == "N":
                break
        except:
            print()
            print("Valor no válido, digite un numero real")
valor_lista()

lista_ordenada = sorted(lista)

print(lista)

print(f"El mayor número de la lista es: {lista_ordenada[-1]}")

