vLido = []
vPares = []
vImpares = []
while len(vLido) < 10:
    n = int(input("Digite um número: "))
    vLido.append(n)
    if n % 2 == 0 and n != 0:
        vPares.append(n)
    elif n % 2 != 0 and n != 0:
        vImpares.append(n)
print(f"A lista digitada foi: {vLido}")
print(f"A lista de números pares é: {vPares}")
print(f"A lista de números ímpares é: {vImpares}")