import random
nEscolhidos = []
while len(nEscolhidos) < 6:
    n = random.randint(1,60)
    if n not in nEscolhidos:
        nEscolhidos.append(n)
#print(nEscolhidos)
escolha = []
while len(escolha) < 6:
    entrada = int(input('Número Escolhido: '))
    if entrada not in escolha:
        escolha.append(entrada)
#print(escolha)
if nEscolhidos == escolha:
    print(f"Acertou\n{nEscolhidos} foram são os números da megasena\n{escolha} foram seus numeros escolidos")
elif nEscolhidos != escolha:
    print(f"Errou\n{nEscolhidos} eram os números corretos\n{escolha} foram os números escolhidos\n"
          f"{set(nEscolhidos) & set(escolha)} são os números acertados")