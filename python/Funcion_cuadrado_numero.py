lista_num = []
lista_cuadrados = []

def cuadrados_lista():
    while True:
        try:
            num =int(input("Digite un número: "))
            lista_num.append(num)
            
            while True:
                again = int(input("¿Desea digitar otro número? 1(si) 2(no): "))
                if again == 2:
                    break
                elif again == 1:
                    print()
                    break
                else:
                    print("\nNúmero no válido\n")
            if again == 2:
                break
        except:
            print("Número no válido\n")
    print(f"\nLa lista es: {lista_num}\n")
    
    for i in lista_num:
        lista_cuadrados.append(i**2)
    print(f"La lista con lo números al cuadrado es: {lista_cuadrados}")
cuadrados_lista()