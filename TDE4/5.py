lista = []
listaPares = []
while len(lista) < 4:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        listaPares.append(num)
    else:
        lista.append(num)
print(f"A soma dos números pares é: {sum(listaPares)}")