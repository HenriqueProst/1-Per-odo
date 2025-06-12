lista = []
while len(lista) < 10:
    n = int(input("Digite um número: "))
    lista.append(n)
    print(f"{sum(lista) / len(lista):.2f} é a média dos números digitados.")