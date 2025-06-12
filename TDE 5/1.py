print("Os nomes das cidade nao tem acento e nao apresentam letra maiscula")
matriz = [["X","curitiba", "florianopolis", "porto alegre", "sao paulo", "rio de janeiro"],
          ["curitiba", 0, 310, 716, 408, 852],
          ["florianopolis",310, 0, 470, 705, 1144],
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

        else:print("Tente Novamente")
        repeticao = int(input("[1] Continuar \n[2] Parar"))
    print(f"As cidades escolhidas foram {lista_cidades}")
    print(f"A distancia total do trajeto é de {sum(lista_distancia)} Km")

