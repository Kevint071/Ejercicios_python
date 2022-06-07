import random as r

lista_impar_int = []
lista_impar_str = []

for i in range(1, 101):
    num = r.randint(0, 100)
    
    if num % 2 != 0:
        lista_impar_int.append(num)

print(f"Los números impares son: \n")

lista_impar_int.sort()

for i in lista_impar_int:
    lista_impar_str.append(str(i))

s = " - ".join(lista_impar_str)

print(s)