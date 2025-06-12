import random
num = int(input("Digite um número: "))
triangular = 0
lista = []
while num != triangular and len(lista) < num :
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