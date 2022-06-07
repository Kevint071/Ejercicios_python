nombre_archivo = input("Ingrese el nombre del archivo: ")

partes_archivo = nombre_archivo.split(".")

partes = {

    "Nombre del archivo": partes_archivo[0],
    "Extensión del archivo": partes_archivo[-1]

}

print(partes)