Abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

Lista_Abecedario = []

Palabra_usuario = input("Digite la palabra que quiera: ")
Palabra_usuario = Palabra_usuario.lower()

Lista_palabra_usuario = []

for i in Palabra_usuario:
    Lista_palabra_usuario.append(i)

for j in range(0, len(Palabra_usuario)):
    for i in range(0, len(Abecedario)):
        if Abecedario[i] != Lista_palabra_usuario[j] and Lista_palabra_usuario[j].count(Abecedario[i]) == 0:
            Lista_Abecedario.append(Abecedario[i])

print(Lista_Abecedario)

# Resolver para mas tarde