lista1 = []
lista2 = []

while True:
    num1 = input(f"Digite un número para la lista 1: ")
    lista1.append(num1)
    while True:
        si_no = int(input("¿Desea digitar otro número? 1(si) 2(no): "))
        if si_no == 2 or si_no == 1:
            break
        elif si_no != 1:
            print("\nEl número especificado no es válido")
    if si_no == 2:
        break
    else:
        print()

while True:
    num2 = input(f"\nDigite un número para la lista 2: ")
    lista2.append(num2)
    
    while True:
        si_no = int(input("¿Desea digitar otro número? 1(si) 2(no): "))
        if si_no == 2 or si_no == 1:
            break
        elif si_no != 1:
            print("\nEl número especificado no es válido")
    if si_no == 2:
        break
    else:
        print()

for i in lista1:
    for j in lista2:
        if j == i:
            break
    if j == i:
        n = 1
        break

if n == 1:
    print("\nTrue")
else:
    print("\nFalse")    
        