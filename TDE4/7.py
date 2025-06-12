lista = []
while len(lista) < 10:
    num = int(input("Digite um número: "))
    lista.append(num)
print(f"A media da lista é: {sum(lista) / len(lista)} \n O maior número é: {max(lista)} \n O menor número é: {min(lista)}")