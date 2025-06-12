def antecessor_sucessor():
    numero = int(input('Informe um número: '))
    print(f"Antecessor: {numero - 1}\nSucessor: {numero + 1}")


def idade_em_2025():
    ano = int(input('Informe seu ano de nascimento: '))
    print(f"No ano de 2025 você terá {2025 - ano} anos")


def salario_minimo():
    salario = float(input("Digite o salário: "))
    print(f"Você recebe {salario / 1518:.2f} salários mínimos")


def valor_produto():
    produto = float(input("Digite o valor do produto: "))
    print(f"{produto * 0.95:.2f} é o valor à vista")
    print(f"{produto / 2:.2f} é o valor parcelado em 2 vezes")
    print(f"{(produto * 1.05) / 3:.2f} é o valor parcelado em 3 vezes com juros")


def consumo_combustivel():
    distancia = float(input("Digite a distância em quilômetros: "))
    litros = float(input("Digite a quantidade de litros utilizados: "))
    print(f"A média de consumo é {distancia / litros:.2f} km/l")


def calcular_latas_tinta():
    altura = float(input("Digite a altura em metros: "))
    raio = float(input("Digite o raio em metros: "))
    lata = 3 * 5  # 3m² por litro, 5 litros por lata
    area = 2 * 3.14 * raio * (raio + altura)
    quantidade_latas = area / lata
    print(f"A quantidade de latas necessárias para cobrir a área é {quantidade_latas:.2f} latas")
    print(f"O valor total é R${quantidade_latas * 50:.2f} reais")

escolha = int(input("Opção: "))
if escolha == 1:
    antecessor_sucessor()
elif escolha == 2:
    idade_em_2025()
elif escolha == 3:
    salario_minimo()
elif escolha == 4:
    valor_produto()
elif escolha == 5:
    consumo_combustivel()
elif escolha == 6:
    calcular_latas_tinta()
else:
    print("Opção inválida")