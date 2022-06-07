lista_nombre = ["K", "e", "v", "i", "n"]

#Se crea una variable de texto vacia y se le añaden las letras una por una

nombre_junto_for = ""

for i in lista_nombre:
    nombre_junto_for = nombre_junto_for + i
print(nombre_junto_for)

#El método join junta todas las letras de una lista ya que no hay un caracter que los separe

nombre_junto_join = "".join(lista_nombre)
print(nombre_junto_join)