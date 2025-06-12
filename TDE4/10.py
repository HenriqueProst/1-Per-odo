import random
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
print(listaPares+listaImpares)