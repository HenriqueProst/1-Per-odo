altura = float(input("Digite a altura em metros: "))
raio = float(input("Digite o raio em metros: "))
lata = 3 * 5
area = 2 * 3.14 * raio * (raio + altura)
quantidade_latas = area / lata
print(f"A quantidade de latas necessárias para cobrir a área é {quantidade_latas} latas \nO valor total é {quantidade_latas * 50} reais")