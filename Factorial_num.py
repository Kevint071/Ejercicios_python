while True:
    num = float(input("Digite un número: "))

    print()
    
    if num % 1 != 0:
        print("El número no es válido")

    if num % 1 == 0:
        num = int(num)
        _num = num
        c = 1
        for i in range(1, _num+1):
            c = c * i
        print(f"El factorial de {num} es {c}")
        break