cadena = "Python"
s = []

for i in range (len(cadena)-1, -1, -1):
    print(cadena[i], end = "")
    s.append(cadena[i])

print()

print(s)

# Join asi como está, convierte los valores de una lista en todos juntos como texto string

s = "".join(s)

print(s)

# El array de una variable hace que se cuente cuanta distancia se van a mostrar los valores de una cadena string y en que sentido

print(s[::-1])
