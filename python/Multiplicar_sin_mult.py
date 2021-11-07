print("Digite 2 números")

def multiplicar (n1, n2):
    Acum = 0
    for i in range(0, n2, 1):
        Acum = Acum + n1
    print(f"El resultado de la multiplicacion es: {Acum}")
multiplicar (int(input("Digite el número 1: ")), int(input("Digite el número 2: ")))