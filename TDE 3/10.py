escolha = int(input('Escolha a moeda para conversão:\n1 - Dólar\n2 - Euro\n3 - Libra\n'))
quantidade = float(input('Informe o quanto você deseja receber: '))
def conversao(taxao):
    global taxa
    if taxao < 1000:
        taxa = 0.05
    elif taxao > 1000:
        taxa = 0.3
    return taxa
if escolha == 1:
    valor = quantidade * 5.65
    taxa = conversao(valor)
    print(f"Voce precisa pagar {valor + (valor * taxa):.2f} reais")
elif escolha == 2:
    valor = quantidade * 6.25
    taxa = conversao(valor)
    print(f"Voce precisa pagar {valor + (valor * taxa):.2f} reais")
elif escolha == 3:
    valor = quantidade * 7.50
    taxa = conversao(valor)
    print(f"Voce precisa pagar {valor + (valor * taxa):.2f} reais")