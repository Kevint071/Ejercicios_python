while True:

    contraseña = input("Digite una contraseña: ")
    print()

    if contraseña.count("a") > 1:
        print('La contraseña solo puede tener una "a"')
        
    if contraseña.count("5") < 1:
        print('La contraseña debe contener el número 5')

    if len(contraseña) < 5:
        print('La contraseña debe contener minimo 5 caracteres')
    
    if contraseña.count("a") <= 1 and contraseña.count("5") >= 1 and len(contraseña) >= 5:
        print("Felicitaciones, contraseña aceptada")
        break