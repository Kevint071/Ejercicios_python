values = [1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1]
for i in values[:]:
    if i == 1:
        values.remove(i)
print(values)

values = [1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1]

j = 0
for i in range(len(values)):
    if values[i-j] == 1:
        values.remove(values[i-j])
        j += 1
print(values)

lista = [1, 2, 1, 2, 1, 2, 1]

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])
    if lista[i] == 1:
        lista.remove(lista[i])

print(lista)

abecedario = ["s", "a", "d", "g", "t", "e", "r", "h"]

x = []

for i in range(0, len(abecedario)-1):
    x.append(abecedario[i])
print(x)

