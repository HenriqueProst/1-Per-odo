import random

def mega_sena():
    nEscolhidos = []
    while len(nEscolhidos) < 6:
        n = random.randint(1, 60)
        if n not in nEscolhidos:
            nEscolhidos.append(n)
    escolha = []
    while len(escolha) < 6:
        entrada = int(input('Número Escolhido: '))
        if entrada not in escolha:
            escolha.append(entrada)
    if nEscolhidos == escolha:
        print(f"Acertou\n{nEscolhidos} foram são os números da megasena\n{escolha} foram seus numeros escolidos")
    elif nEscolhidos != escolha:
        print(f"Errou\n{nEscolhidos} eram os números corretos\n{escolha} foram os números escolhidos\n"
              f"{set(nEscolhidos) & set(escolha)} são os números acertados")

def ordenar_com_min():
    lista = []
    lista2 = []
    while len(lista) < 20:
        num = random.randint(1, 100)
        lista.append(num)
    print(lista)
    while len(lista2) < 20:
        menorNum = min(lista)
        lista.remove(menorNum)
        lista2.append(menorNum)
    print(lista2)

def maior_que_soma_outros_dois():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    if num1 > (num2 + num3):
        print("O primeiro número é MAIOR que a soma dos outros dois.")
    elif num2 > (num1 + num3):
        print("O segundo número é MAIOR que a soma dos outros dois.")
    elif num3 > (num1 + num2):
        print("O terceiro número é MAIOR que a soma dos outros dois.")
    else:
        print("Nenhum dos números é maior que a soma dos outros dois.")

def operacoes_basicas():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    lista = [num1, num2]
    print(f"A soma dos números é: {num1 + num2} \nO produto dos números é: {num1 * num2} \nO quociente dos números é: {num1/num2}")

def soma_dos_pares():
    lista = []
    listaPares = []
    while len(lista) < 4:
        num = int(input("Digite um número: "))
        if num % 2 == 0:
            listaPares.append(num)
        else:
            lista.append(num)
    print(f"A soma dos números pares é: {sum(listaPares)}")

def verificar_numero_triangular():
    num = int(input("Digite um número: "))
    triangular = 0
    lista = []
    while num != triangular and len(lista) < num:
        num2 = random.randint(1, num)
        triangular = (num2 * (num2 + 1) * (num2 + 2))
        lista.append(triangular)
        if num > 0:
            if triangular == num:
                print(f"O número {num} é triangular.")
        else:
            print("Número inválido.")
    if num < 0:
        print("Número inválido.")
    elif num != triangular:
        print(f'O número {num} não é triangular')

def media_maior_menor():
    lista = []
    while len(lista) < 10:
        num = int(input("Digite um número: "))
        lista.append(num)
    print(f"A media da lista é: {sum(lista) / len(lista)} \n O maior número é: {max(lista)} \n O menor número é: {min(lista)}")

def procurar_numero_na_lista():
    lista = [random.randint(1, 100) for _ in range(10)]
    escolha = int(input('Escolha [1] Para procurar um número na lista ou [2] Para não procurar: '))
    if escolha == 1:
        num2 = int(input("Digite um número: "))
        if num2 in lista:
            posicoes = [i + 1 for i, n in enumerate(lista) if n == num2]
            print(f'O número {num2} está na lista. Ele aparece {len(posicoes)} vez(es).')
            print(f'Ele aparece nas posições: {", ".join(map(str, posicoes))}')
        else:
            print(f'O número {num2} não está na lista.')
    elif escolha == 2:
        print('Você não escolheu procurar um número na lista.')
    else:
        print('Opção inválida.')

def separar_pares_e_impares():
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

def ordenar_lista_pares_impares():
    num = random.randint(1, 100)
    lista = []
    listaPares = []
    listaImpares = []
    while len(lista) < 10:
        num = random.randint(1, 100)
        lista.append(num)
        if num % 2 == 0:
            listaPares.append(num)
        elif num % 2 != 0:
            listaImpares.append(num)
    listaPares.sort()
    listaImpares.sort()
    print(lista)
    print(listaPares + listaImpares)

def tabuada_1():
    for i in range(1, 11):
        print(f"1 x {i} = {1 * i}")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    mega_sena()
elif opcao == 2:
    ordenar_com_min()
elif opcao == 3:
    maior_que_soma_outros_dois()
elif opcao == 4:
    operacoes_basicas()
elif opcao == 5:
    soma_dos_pares()
elif opcao == 6:
    verificar_numero_triangular()
elif opcao == 7:
    media_maior_menor()
elif opcao == 8:
    procurar_numero_na_lista()
elif opcao == 9:
    separar_pares_e_impares()
elif opcao == 10:
    ordenar_lista_pares_impares()
elif opcao == 11:
    tabuada_1()
else:
    print("Opção inválida. Tente novamente.")