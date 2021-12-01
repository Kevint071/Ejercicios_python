lista_num = []
def media_lista():
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
    lista_num.sort()
    print(f"La lista es: {lista_num}\n")
    
    media = sum(lista_num)/len(lista_num)
        
    print(f"La media de la lista es {media:g}")

media_lista()