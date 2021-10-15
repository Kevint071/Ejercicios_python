lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
y = 0

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        x = x + 1
    elif lista[i] % 2 != 0:
        y = y + 1

print(f"Números pares: {x}")
print(f"Números impares: {y}")