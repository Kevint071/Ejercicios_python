def factorial(num):
    Acumulador = 1
    for i in range(1, num+1):
        Acumulador = Acumulador * i
    print(f"El factorial de {num} es {Acumulador}")
    
while True:
    factorial(int(input("Digite un número: ")))
    
    again = int(input("\n¿Desea digitar otro número? 1(si) 2(no): "))
    while True:
        if again == 1 or again == 2:
            break
        else:
            print("\nNúmero no válido")
            again = int(input("\n¿Desea digitar otro número? 1(si) 2(no): "))
    if again != 1 and again == 2:
            break