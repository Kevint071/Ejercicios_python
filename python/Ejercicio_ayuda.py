while True:
    try:
        print("Digite los puntos de la esquina superior derecha: ")
        x_lim = int(input("Digite la longitud: "))
        y_lim = int(input("Digite la latitud: "))
        
        print("Coloque los puntos de la coordenada en que está: ")
        
        x_punto = int(input('Digite la coordenada "x": '))
        y_punto = int(input('Digite la coordenada "y": '))
        
        if x_punto >= x_lim or y_punto >= y_lim:
            print("La coordenada ingresada se salió de el límite")
        if x_punto < x_lim and y_punto < y_lim:
            break
    except:
        print("Las coordenadas ingresadas no son válidas")
derecho = "derecho"
superior = "superior"
izquierdo = "izquierdo"
inferior = "inferior"

x = x_punto < (x_lim/2)
y = y_punto < (y_lim/2)
div_x = 1 - (x_punto / x_lim)
div_y =1 - (y_punto / y_lim)

if x == True and y == False:
    if div_x < div_y:
        print(f"El borde mas cerca es el borde {izquierdo}")
    else:
        print(f"El borde mas cerca es el borde {superior}")

if x == False and y == False:
    if div_x < div_y:
        print(f"El borde mas cerca es el borde {derecho}")
    else:
        print(f"El borde mas cerca es el borde {inferior}")

if x == False and y == True:
    if div_x < div_y:
        print(f"El borde mas cerca es el borde {derecho}")
    else:
        print(f"El borde mas cerca es el borde {superior}")

if x == True and y == True:
    if div_x < div_y:
        print(f"El borde mas cerca es el borde {izquierdo}")
    else:
        print(f"El borde mas cerca es el borde {superior}")