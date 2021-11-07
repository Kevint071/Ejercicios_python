num1 = float(input("Digite el primer numero: "))
num2 = float(input("Digite el segundo numero: "))

if num1 % 1 == 0:
    num1 = int(num1)

if num1 % 1 != 0:
    num1 = (f"{num1:g}")
    num1 = float(num1)

if num2 % 1 == 0:
    num2 = int(num2)

if num2 % 1 != 0:
    num2 = (f"{num2:g}")
    num2 = float(num2)

print()

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

suma = (f"{suma:g}")


print(f"La suma de los 2 numeros es: {suma}")
print(f"La resta de los 2 numeros es " + "{:g}".format(resta))
print(f"La multiplicacion de los 2 numeros es {mult:g}")
print(f"La división de los 2 números es {div:g}")

print(float(suma))

if float(suma) % 1 == 0:
    suma = int(suma)

elif float(suma) % 1 != 0:
    suma = float(suma)

print(type(suma))
