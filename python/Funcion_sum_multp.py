def elegir_operacion(palabra):
    datos = int(input(f"Digite la cantidad de datos que quiere {palabra}: "))
    numeros = []

    print()

    for i in range(1, datos+1):
        nums = float(input(f"Digite el dato {i}: "))
        numeros.append(nums)
    
    return numeros


def sum(lista):
    acum = 0
    for i in lista:
        acum += i
    return acum


def mult(lista):
    acum = 1
    for i in lista:
        acum *= i
    return acum

def run():
    print("""Digite la operacion:

    1. Suma
    2. Multiplicacion
    """)

    opcion = int(input("Digite la operacion que quiere: "))

    if opcion == 1:
        lista_num = elegir_operacion("sumar")
        print(f"\nLa suma de los números escritos es: {sum(lista_num):g}")

    elif opcion == 2:
        lista_num = elegir_operacion("multiplicar")
        print(f"\nLa multiplicación de los números escritos es: {mult(lista_num):g}")


if __name__ == "__main__":
    run()