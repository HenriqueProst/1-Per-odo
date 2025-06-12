from random import randint
from getpass import getpass  # Oculta a entrada do jogador

vitoria = empate = derrota = 0
continuar = 1
while continuar == 1:
    itens = ('Pedra', 'Papel', 'Tesoura')

    print("Escolha o modo de jogo:")
    print("[1] Contra o computador")
    print("[2] Contra outro jogador")
    modo = int(input("Modo: "))

    if modo == 1:
        jogador1_nome = input("Nome do jogador: ")
        jogador2_nome = "Computador"
    else:
        jogador1_nome = input("Jogador 1, informe seu nome: ")
        jogador2_nome = input("Jogador 2, informe seu nome: ")

    print('0: Pedra, 1: Papel, 2: Tesoura')

    if modo == 1:
        jogador1_escolha = int(input(f'{jogador1_nome}, sua escolha: '))
        jogador2_escolha = randint(0, 2)
        print(f"{jogador2_nome} escolheu: {itens[jogador2_escolha]}")
    else:
        jogador1_escolha = int(getpass(f'{jogador1_nome}, escolha (oculto): '))
        jogador2_escolha = int(getpass(f'{jogador2_nome}, escolha (oculto): '))
        print(f"{jogador2_nome} fez sua escolha!")
    print(f"{jogador1_nome} escolheu: {itens[jogador1_escolha]}")
    print(f"{jogador2_nome} escolheu: {itens[jogador2_escolha]}")

    resultado = (jogador1_escolha - jogador2_escolha) % 3
    if resultado == 0:
        print('Empate')
        empate += 1
    elif resultado == 1:
        print(f'Vitória de {jogador1_nome}!')
        vitoria += 1
    else:
        print(f'Vitória de {jogador2_nome}!')
        derrota += 1

    continuar = int(input('[1] Continuar [2] Parar: '))
if continuar != 1 or 2: print('Opção invalida')

print(f"{vitoria} vitórias, {empate} empates, {derrota} derrotas")