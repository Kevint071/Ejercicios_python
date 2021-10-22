N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
N3 = int(input("Número 3: "))
N4 = int(input("Número 4: "))

if N1 > N2 and N1 > N3 and N1 > N4:
    print(f"El número mayor es N1({N1})")

elif N1 == N2 and N1 > N3 and N1 > N4:
    print(f"Los números mayores son N1({N1}) y N2({N2})")

elif N1 > N2 and N1 == N3 and N1 > N4:
    print(f"Los números mayores son N1({N1}) y N3({N3})")

elif N1 > N2 and N1 > N3 and N1 == N4:
    print(f"Los números mayores son N1({N1}) y N4({N4})")

elif N2 > N1 and N2 > N3 and N2 > N4:
    print(f"El número mayor es N2({N2})")

elif N2 > N1 and N2 == N3 and N2 > N4:
    print(f"Los números mayores son N2({N2}) y N3({N3})")

elif N2 > N1 and N2 > N3 and N2 == N4:
    print(f"Los números mayores son N2({N2}) y N4({N4})")

elif N3 > N1 and N3 > N2 and N3 > N4:
    print(f"El número mayor es N3({N3})")

elif N3 > N1 and N3 > N2 and N3 == N4:
    print(f"Los números mayores son N3({N3}) y N4({N4})")

elif N4 > N1 and N4 > N2 and N4 > N3:
    print(f"El número mayor es N4({N4})")
