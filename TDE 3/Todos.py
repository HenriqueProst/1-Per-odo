def impares_ate_100():
    for i in range(1, 100, 2):
        print(i)


def decrescente_de_50():
    for i in range(50, -1, -5):
        print(i)


def multiplos_de_10():
    for i in range(-100, 101, 10):
        print(i)


def divisiveis_por_4():
    for i in range(1, 100):
        if i % 4 == 0:
            print(i)


def impares_ate_n():
    numero = int(input("Informe um número: "))
    for i in range(1, numero):
        if i % 2 != 0:
            print(i)


def polegadas_para_cm():
    for i in range(1, 21):
        cm = i * 2.54
        print(f"{i} polegadas é igual a {cm:.2f} centímetros")


def km_para_milhas():
    for i in range(20, 161, 10):
        m = i * 0.62137
        print(f'{m:.2f} milhas = {i:.2f} Km')


def media_numeros_digitados():
    lista = []
    while len(lista) < 10:
        n = int(input("Digite um número: "))
        lista.append(n)
        print(f"{sum(lista) / len(lista):.2f} é a média dos números digitados.")


def multiplos_de_3_entre_limites():
    li = int(input('Digite o limite inicial: '))
    lf = int(input('Digite o limite final: '))
    for i in range(li + 1, lf):
        if i % 3 == 0:
            print(i)


def conversao_moeda():
    escolha1 = int(input('Escolha a moeda para conversão:\n1 - Dólar\n2 - Euro\n3 - Libra\n'))
    quantidade = float(input('Informe o quanto você deseja receber: '))

    def conversao(taxao):
        global taxa
        if taxao < 1000:
            taxa = 0.05
        elif taxao > 1000:
            taxa = 0.3
        return taxa

    if escolha1 == 1:
        valor = quantidade * 5.65
        taxa = conversao(valor)
        print(f"Voce precisa pagar {valor + (valor * taxa):.2f} reais")
    elif escolha1 == 2:
        valor = quantidade * 6.25
        taxa = conversao(valor)
        print(f"Voce precisa pagar {valor + (valor * taxa):.2f} reais")
    elif escolha1 == 3:
        valor = quantidade * 7.50
        taxa = conversao(valor)
        print(f"Voce precisa pagar {valor + (valor * taxa):.2f} reais")


def tabuada_1():
    for i in range(1, 11):
        print(f"1 x {i} = {1 * i}")

escolha = int(input("Opção: "))
if escolha == 1:
    impares_ate_100()
elif escolha == 2:
    decrescente_de_50()
elif escolha == 3:
    multiplos_de_10()
elif escolha == 4:
    divisiveis_por_4()
elif escolha == 5:
    impares_ate_n()
elif escolha == 6:
    polegadas_para_cm()
elif escolha == 7:
    km_para_milhas()
elif escolha == 8:
    media_numeros_digitados()
elif escolha == 9:
    multiplos_de_3_entre_limites()
elif escolha == 10:
    conversao_moeda()
elif escolha == 11:
    tabuada_1()
else:
    print("Opção inválida")