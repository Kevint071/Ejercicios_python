# n = float(input("Digite un número: "))

# nn = (f"{n}{n}")

# nnn = (f"{n}{n}{n}")

# n, nn, nnn = int(n), int(nn), int(nnn)

# suma = n + nn + nnn

# print(f"La suma de los numeros ({n} + {nn} + {nnn}) es = {suma}")

n = input("Digite un número: ")

nn = int("%s%s"% (n, n))

nnn = int("%s%s%s"% (n, n, n))

n, nn, nnn = int(n), int(nn), int(nnn)

suma = n + nn + nnn

print(f"La suma de los numeros ({n} + {nn} + {nnn}) es = {suma}")
