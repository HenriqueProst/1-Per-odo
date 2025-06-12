import random

def mega_sena():
    n_escolhidos = []
    while len(n_escolhidos) < 6:
        n = random.randint(1, 60)
        if n not in n_escolhidos:
            n_escolhidos.append(n)
    escolha = []
    while len(escolha) < 6:
        entrada = int(input('Número Escolhido: '))
        if entrada not in escolha:
            escolha.append(entrada)
    if n_escolhidos == escolha:
        print(f"Acertou\n{n_escolhidos} foram são os números da megasena\n{escolha} foram seus numeros escolidos")
    elif n_escolhidos != escolha:
        print(f"Errou\n{n_escolhidos} eram os números corretos\n{escolha} foram os números escolhidos\n"
              f"{set(n_escolhidos) & set(escolha)} são os números acertados")

def ordenar_com_min():
    lista = []
    lista2 = []
    while len(lista) < 20:
        num = random.randint(1, 100)
        lista.append(num)
    print(lista)
    while len(lista2) < 20:
        menor_num = min(lista)
        lista.remove(menor_num)
        lista2.append(menor_num)
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
    print(f"A soma dos números é: {num1 + num2} \nO produto dos números é: {num1 * num2} \nO quociente dos números é: {num1/num2}")

def soma_dos_pares():
    lista = []
    lista_pares = []
    while len(lista) < 4:
        num = int(input("Digite um número: "))
        if num % 2 == 0:
            lista_pares.append(num)
        else:
            lista.append(num)
    print(f"A soma dos números pares é: {sum(lista_pares)}")

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
    v_lido = []
    v_pares = []
    v_impares = []
    while len(v_lido) < 10:
        n = int(input("Digite um número: "))
        v_lido.append(n)
        if n % 2 == 0 and n != 0:
            v_pares.append(n)
        elif n % 2 != 0 and n != 0:
            v_impares.append(n)
    print(f"A lista digitada foi: {v_lido}")
    print(f"A lista de números pares é: {v_pares}")
    print(f"A lista de números ímpares é: {v_impares}")

def ordenar_lista_pares_impares():
    random.randint(1, 100)
    lista = []
    lista_pares = []
    lista_impares = []
    while len(lista) < 10:
        num = random.randint(1, 100)
        lista.append(num)
        if num % 2 == 0:
            lista_pares.append(num)
        elif num % 2 != 0:
            lista_impares.append(num)
    lista_pares.sort()
    lista_impares.sort()
    print(lista)
    print(lista_pares + lista_impares)

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
