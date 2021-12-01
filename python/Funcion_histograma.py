lista_num = []

def procedimiento(num):
    print()
    for i in range(1, num+1):
        while True:
            num_lista = int(input(f"Digite el número {i}: "))
            if num_lista > 0:
                lista_num.append(num_lista)
                break
            else:
                print("\nEl número para el histograma no es válido")

    print("\nSu histograma es:\n")

    for i in lista_num:
        print("*" * i)
procedimiento(int(input("Digite cuantos número quiere para el histograma: ")))