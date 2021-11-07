numbers = []

while True:
  num = int(input("Ingrese un número: "))
  numbers.append(num)
  if num == 999: break

print(f"Total de números ingresados: {len(numbers)}")
print(f"Suma de los números ingresados: {sum(numbers)}")
print(f"Promedio de los números ingresados: {sum(numbers)/len(numbers)}")