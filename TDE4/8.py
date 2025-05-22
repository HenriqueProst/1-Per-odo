import random
lista = [random.randint(1, 100) for _ in range(10)]

escolha = int(input('Escolha [1] Para procurar um número na lista ou [2] Para não procurar: '))
if escolha == 1:
    num2 = int(input("Digite um número: "))
    if num2 in lista:
        # Encontrando todas as posições (índices + 1)
        posicoes = [i + 1 for i, n in enumerate(lista) if n == num2]
        print(f'O número {num2} está na lista. Ele aparece {len(posicoes)} vez(es).')
        print(f'Ele aparece nas posições: {", ".join(map(str, posicoes))}')
    else:
        print(f'O número {num2} não está na lista.')
elif escolha == 2:
    print('Você não escolheu procurar um número na lista.')
else:
    print('Opção inválida.')