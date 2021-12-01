print("Bienvenid@\n")

lista = []

for i in range(1, 3):
    num = float(input(f"Digite el número {i}: "))
    
    if num % 1 == 0:
        num = int(num)
    else:
        num = (f"{num:g}")
        num = float(num)
        
    lista.append(num)

print()
print(lista)
print()

lista.sort()

num1, num2 = lista

for i in range(num1, num2+1):
    print(f"Cuadrado de {i} = {i**2}")