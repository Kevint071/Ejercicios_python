while True:
    try:
        num = float(input("Digite un número: "))
        break
    except:
        print("El número ingresado no es válido")

if num % 1 != 0:
    num = (f"{num:g}")
    num = float(num)
        
if num % 1 == 0:
    num = int(num)
            
if num > 1000 and num < 2000:
    num_2 = num - 1000
    if num_2 >= 500:
        print("El número se acerca más al 2000")
    else:
        print("El número se acerca más al 1000")
        
elif num == 1000:
    print("El número es igual a 1000")

elif num == 2000:
    print("El número es igual a 2000")
            
elif num < 1000:
    print("El número se acerca más al 1000")
            
elif num > 2000:
    print("El número se acerca más al 2000")