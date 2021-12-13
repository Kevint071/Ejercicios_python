from random import randint
lista_usuario = []
si_no = 1

while si_no == 1:
    win = None
    lista_usuario.clear()    
    numero = randint(1, 30)
    i = 0

    while i < 7:
        i += 1
        while True:
            try:
                num_usuario = int(input("Intenta adivinar el número que pienso entre 1 y 30: "))
                lista_usuario.append(num_usuario)
                
                if lista_usuario.count(num_usuario) == 2:
                    print("Este número ya lo había dicho, piense otro\n")
                    lista_usuario.remove(num_usuario)
                elif num_usuario > 30 or num_usuario < 1:
                    print("El número que debes adivinar está entre 1 y 30\n")
                else:
                    break 
            except:
                print("Número no válido")

        if num_usuario > numero:
            print("El número en que pienso es mas bajo...\n")
        elif num_usuario < numero:
            print("El número en que pienso es mas alto...\n")
        else:
            win = "Has acertado!\n"
            print(win)
            break
    if win == None:
        print(f"Perdistes... El número en que pensaba era el {numero}\n")
        
    while True:
        try:
            si_no = int(input("¿Desea jugar otra vez? 1(si) 2(no): "))
            
            if si_no == 1 or si_no == 2:
                print()
                break
            else:
                print("El número no es válido\n")
        except:
            print("Por Dios esto no es un número\n")