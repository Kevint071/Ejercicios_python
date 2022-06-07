def repetir_cadena(cadena, veces):
    cadena_final = (cadena + " ") * veces
    print(f"\n{cadena_final}")
repetir_cadena(input("Digite una palabra: "), int(input("Digite el número de veces que se va a repetir la cadena: ")))

