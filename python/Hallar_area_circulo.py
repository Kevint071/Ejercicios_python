import math

radio = float(input("Digite el largo del radio: "))

area = math.pi * (radio ** 2)
print(area)

print("El área del círculo es: {:.4g}".format(area))
print("El área del círculo es: {:.2f}".format(area))