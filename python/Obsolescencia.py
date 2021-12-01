precio_inicial_piezas = []
precio_mes_1 = []
precio_mes_2 = []
precio_mes_3 = []
precio_mes_4 = []
precio_mes_5 = []
precio_mes_6 = []
precio_final_piezas = []

def inicial_final(nombre_precio):
    for i in range(1, 9):
        precio_piezas = float(input(f"Digite el precio {nombre_precio} de la pieza {i}: "))
        
        if precio_piezas % 1 == 0:
            precio_piezas = int(precio_piezas)
        else:
            precio_piezas = (f"{precio_piezas:g}")
            precio_piezas = float(precio_piezas)
        
        precio_inicial_piezas.append(f"{precio_piezas:.2f}")
        precio_mes_1.append(f"{precio_piezas:.2f}")
        precio_piezas = precio_piezas - precio_piezas * 0.02
        precio_mes_2.append(f"{precio_piezas:.2f}")
        precio_piezas = precio_piezas - precio_piezas * 0.02
        precio_mes_3.append(f"{precio_piezas:.2f}")
        precio_piezas = precio_piezas - precio_piezas * 0.02
        precio_mes_4.append(f"{precio_piezas:.2f}")
        precio_piezas = precio_piezas - precio_piezas * 0.02
        precio_mes_5.append(f"{precio_piezas:.2f}")
        precio_piezas = precio_piezas - precio_piezas * 0.02
        precio_mes_6.append(f"{precio_piezas:.2f}")
        precio_piezas = precio_piezas - precio_piezas * 0.02
        precio_final_piezas.append(f"{precio_piezas:.2f}")
        
inicial_final("inicial")

for i in range(0, len(precio_inicial_piezas)):
    if float(precio_inicial_piezas[i]) % 1 == 0:
        precio_inicial_piezas[i] = int(float(precio_inicial_piezas[i]))
    else:
        precio_inicial_piezas[i] = float(precio_inicial_piezas[i])
      
for i in range(0, len(precio_mes_1)):
    if float(precio_mes_1[i]) % 1 == 0:
        precio_mes_1[i] = int(float(precio_mes_1[i]))
    else:
        precio_mes_1[i] = float(precio_mes_1[i])
            
for i in range(0, len(precio_mes_2)):
    if float(precio_mes_2[i]) % 1 == 0:
        precio_mes_2[i] = int(float(precio_mes_2[i]))
    else:
        precio_mes_2[i] = float(precio_mes_2[i])
    
for i in range(0, len(precio_mes_3)):
    if float(precio_mes_3[i]) % 1 == 0:
        precio_mes_3[i] = int(float(precio_mes_3[i]))
    else:
        precio_mes_3[i] = float(precio_mes_3[i])
    
for i in range(0, len(precio_mes_4)):
    if float(precio_mes_4[i]) % 1 == 0:
        precio_mes_4[i] = int(float(precio_mes_4[i]))
    else:
        precio_mes_4[i] = float(precio_mes_4[i])
    
for i in range(0, len(precio_mes_5)):
    if float(precio_mes_5[i]) % 1 == 0:
        precio_mes_5[i] = int(float(precio_mes_5[i]))
    else:
        precio_mes_5[i] = float(precio_mes_5[i])
    
for i in range(0, len(precio_mes_6)):
    if float(precio_mes_6[i]) % 1 == 0:
        precio_mes_6[i] = int(float(precio_mes_6[i]))
    else:
        precio_mes_6[i] = float(precio_mes_6[i])
            
for i in range(0, len(precio_final_piezas)):
    if float(precio_final_piezas[i]) % 1 == 0:
        precio_final_piezas[i] = int(float(precio_final_piezas[i]))
    else:
        precio_final_piezas[i] = float(precio_final_piezas[i])

s = "S/."
piezas = [["Pieza 1", s, precio_inicial_piezas[0], precio_mes_1[0], precio_mes_2[0], precio_mes_3[0], precio_mes_4[0], precio_mes_5[0], precio_mes_6[0], precio_final_piezas[0]], ["Pieza 2", s, precio_inicial_piezas[1], precio_mes_1[1], precio_mes_2[1], precio_mes_3[1], precio_mes_4[1], precio_mes_5[1], precio_mes_6[1], precio_final_piezas[1]], ["Pieza 3", s, precio_inicial_piezas[2], precio_mes_1[2], precio_mes_2[2], precio_mes_3[2], precio_mes_4[2], precio_mes_5[2], precio_mes_6[2], precio_final_piezas[2]], ["Pieza 4", s, precio_inicial_piezas[3], precio_mes_1[3], precio_mes_2[3], precio_mes_3[3], precio_mes_4[3], precio_mes_5[3], precio_mes_6[3], precio_final_piezas[3]], ["Pieza 5", s, precio_inicial_piezas[4], precio_mes_1[4], precio_mes_2[4], precio_mes_3[4], precio_mes_4[4], precio_mes_5[4], precio_mes_6[4], precio_final_piezas[4]], ["Pieza 6", s, precio_inicial_piezas[5], precio_mes_1[5], precio_mes_2[5], precio_mes_3[5], precio_mes_4[5], precio_mes_5[5], precio_mes_6[5], precio_final_piezas[5]], ["Pieza 7", s, precio_inicial_piezas[6], precio_mes_1[6], precio_mes_2[6], precio_mes_3[6], precio_mes_4[6], precio_mes_5[6], precio_mes_6[6], precio_final_piezas[6]], ["Pieza 8", s, precio_inicial_piezas[7], precio_mes_1[7], precio_mes_2[7], precio_mes_3[7], precio_mes_4[7], precio_mes_5[7], precio_mes_6[7], precio_final_piezas[7]]]

Tabla = """
+-------------------------------------------------------------------------------------------------------------------+
| Descripción  |  Precio   |                            Obsolescencia Mensual                           |  Precio   |
|              |  Inicial  |     1     |     2     |     3      |     4      |     5      |     6       |  Final    |
|-------------------------------------------------------------------------------------------------------------------|
{}
+-------------------------------------------------------------------------------------------------------------------+\
"""
Tabla = (Tabla.format("\n".join("| {:<13}|{:<5}{:<6}|    {:<7}|   {:<8}|   {:<9}|   {:<9}|   {:<9}|   {:<9}|   {:<9}|".format(*i) for i in piezas)))
print (Tabla)