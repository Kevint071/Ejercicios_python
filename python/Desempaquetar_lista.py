datos = ("Juan", "Perez", 53.44)
format_string = "Hola "

print("%s%s %s. Tu balance es de %g$"%(format_string, datos[0], datos[1], datos[2]))
print("%s%s %s. Tu balance es de %g$"%(format_string, *datos))
