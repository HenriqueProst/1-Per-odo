import random
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