#Exercicio 1
def matriz_4x4 ():
    import random
    matriz = [[random.randint(0, 100) for ii in range(4)] for i in range(4)]
    lista = []
    vetor = [[random.randint(0, 100) for ii in range(4)] for i in range(4)]
    for i in matriz:
        for j in i:
            lista.append(j)
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j: j + 2] = lista[j + 1], lista[j]
    lista.reverse()
    for i in range(len(vetor)):
        for j in range(len(vetor[i])):
            vetor[i][j] = lista[i * 3 + j]
    # Formatação Primeira Matriz
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()
    print("-" * 20)
    print('Matriz Organizada: ')
    # Formatção Matriz Organizada
    for i in vetor:
        for j in i:
            print(j, end=" ")
        print()
    print("-" * 20)
    print(f"Média aritmética: {sum(lista) / len(lista)}")

#Exercicio 2
def multiplicao ():
    import random
    matriz = [[random.randint(0, 100) for ii in range(4)] for i in range(4)]
    # formatacao
    print("Matriz Original:")
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()
    print("_" * 20)
    # Multiplicador do usuario
    multiplicador = int(input('Insira o numero que deseja multiplicar a matriz: '))
    for i in matriz:
        for j in i:
            j = j * multiplicador  # Multpiplica J para depois printar na matriz
            print(j, end=" ")
        print()

#Exercicio 3
def maior_menor():
    import random as rd
    matriz = [[" " for i in range(4)] for i in range(4)]
    lista = []
    maior = 99
    menor = 1000
    coluna = 0
    for i in matriz:
        for j in matriz:
            num = rd.randint(100, 999)  # Gera um numero aleatorio no intervalo
            if num not in lista:  # Verifica se o numero gerado tem na lista e o adiciona se nao tiver
                lista.append(num)
    # Transforma a lista em matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = lista[i * 4 + j]
    # verifica o maior numero da matriz
    for i in matriz:
        for j in i:
            if j > maior:
                maior = j
    # Descobre a coluna do maior numero da matriz
    for i, linha in enumerate(matriz):
        if maior in linha:
            coluna = linha.index(maior)
        # Descobre o menor numero da coluna do maior numero
        for ii in range(len(matriz)):
            colunaM = matriz[ii][coluna]
            if colunaM < menor:
                menor = colunaM
    # Formatacao
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()
    print("_" * 20)
    print()
    print(f"O maior número da matriz é {maior}\nMenor número de sua coluna é {menor}")

#Exercicio 4
def lista_hacharuda():
    import random as rd
    import numpy as np
    matriz = np.array([[rd.randint(10, 99) for ii in range(5)] for i in range(5)])
    lista = ["-"] * len(matriz) ** 2
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

    def letra_a():
        coluna_a_ignorar = 2
        print("-" * 20)
        for i in range(matriz.shape[0]):
            for j in range(matriz.shape[1]):
                if i != coluna_a_ignorar and j != coluna_a_ignorar:
                    matriz[i, j] = 0

    def letra_b():
        print("-" * 20)
        for i in range(matriz.shape[0]):
            for j in range(matriz.shape[1]):
                if (i != 0 and i != 4) and (j != 0 and j != 4):
                    matriz[i, j] = 0

    def letra_c():
        print("-" * 20)  # mais formatacao
        for i in range(5):
            for j in range(5):
                if abs(i - j) != 1:  # abs serve para impedir de ficar negativo o resultado
                    matriz[i][j] = 0

    def letra_d():
        print("-" * 20)
        for i in range(matriz.shape[0]):
            for j in range(matriz.shape[1]):
                for ii in [1, 3]:
                    for jj in [1, 3]:
                        matriz[ii][jj] = 0
                        if i % 2 == 0 and j % 2 == 0:
                            matriz[i, j] = 00

    print("_" * 20)
    escolha = int(input("Escolha de 1 ate 4: "))
    if escolha == 1:
        letra_a()
    elif escolha == 2:
        letra_b()
    elif escolha == 3:
        letra_c()
    elif escolha == 4:
        letra_d()
    # Formatacao padrao
    for i in matriz:
        for j in i:
            if j == 0:
                j = "  "
            print(j, end=" ")
        print()

#Exercicio  5
def pares_impares():
    import random as rd
    matriz = [[rd.randint(10, 99) for ii in range(15)] for i in range(7)]
    lista = []
    listaPares = []
    listaImpares = []
    # Formatacao
    for i in matriz:
        for j in i:
            lista.append(j)
            print(j, end=" ")
        print()
    # Separa entre impares e pares
    for i in matriz:
        for j in i:
            n = int(j)
            if n % 2 == 0:
                listaPares.append(n)
            else:
                listaImpares.append(n)
    # Organiza as lista e depois as transforma na lista principal
    listaPares.sort();listaImpares.sort()
    lista = listaPares + listaImpares
    # Transforma a lista em matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = lista[i * 15 + j]
    # Formatacao
    print("Matriz organizada: ")
    print("_" * 44)
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

#Exercicio 6
def distancia_cidades():
    print("Os nomes das cidade nao tem acento e nao apresentam letra maiscula")
    matriz = [["X", "curitiba", "florianopolis", "porto alegre", "sao paulo", "rio de janeiro"],
              ["curitiba", 0, 310, 716, 408, 852],
              ["florianopolis", 310, 0, 470, 705, 1144],
              ["porto alegre", 716, 470, 0, 1119, 1553],
              ["sao paulo", 408, 705, 1119, 0, 429],
              ["rio de janeiro", 852, 1144, 1553, 429, 0]]
    lista = []
    primeira_cidade = 0
    segunda_cidade = 0
    cidade_inicio = input("Informe a cidade de inicio: ")
    cidade_final = input("Informe  a cidade final: ")
    for i in matriz:
        for j in i:
            lista.append(j)
    if cidade_inicio in lista or cidade_final in lista:
        primeira_cidade = lista.index(cidade_inicio)
        segunda_cidade = lista.index(cidade_final) - 6
    else:
        print("Tente Novamente")

    distancia = matriz[primeira_cidade][segunda_cidade]
    print(distancia)
    velocidade = float(input("Informe a velocidade media em Km/h"))
    print(f"Voce ira demorar aproximadamente {distancia / velocidade} horas")

#Exercicio 7
def distancia_total_cidades():
    print("Os nomes das cidade nao tem acento e nao apresentam letra maiscula")
    matriz = [["X", "curitiba", "florianopolis", "porto alegre", "sao paulo", "rio de janeiro"],
              ["curitiba", 0, 310, 716, 408, 852],
              ["florianopolis", 310, 0, 470, 705, 1144],
              ["porto alegre", 716, 470, 0, 1119, 1553],
              ["sao paulo", 408, 705, 1119, 0, 429],
              ["rio de janeiro", 852, 1144, 1553, 429, 0]]
    lista = []
    lista_cidades = []
    lista_distancia = []
    primeira_cidade = 0
    segunda_cidade = 0
    repeticao = 0

    for i in matriz:
        for j in i:
            lista.append(j)

    cidade_inicio = input("Informe a cidade de inicio: ")

    if cidade_inicio not in lista:
        print("tente novamente")
        repeticao = 2

    elif cidade_inicio in lista:
        lista_cidades.append(cidade_inicio)
        while repeticao != 2:
            cidade_final = input("Informe  a proxima cidade: ")
            if cidade_inicio in lista and cidade_final in lista:
                primeira_cidade = lista.index(cidade_inicio)
                segunda_cidade = lista.index(cidade_final) - 6
                distancia = matriz[primeira_cidade][segunda_cidade]
                print(distancia)
                lista_distancia.append(distancia)
                lista_cidades.append(cidade_final)

            else:
                print("Tente Novamente")
            repeticao = int(input("[1] Continuar \n[2] Parar"))
        print(f"As cidades escolhidas foram {lista_cidades}")
        print(f"A distancia total do trajeto é de {sum(lista_distancia)} Km")


entrada = int(input("Escolha um exercicio: "))
if entrada == 1:
    matriz_4x4()
elif entrada == 2:
    multiplicao()
elif entrada == 3:
    maior_menor()
elif entrada == 4:
    lista_hacharuda()
elif entrada == 5:
    pares_impares()
elif entrada == 6:
    distancia_cidades()
elif entrada == 7:
    distancia_total_cidades()
else:print("Opção Inválida")