li = int(input('Digite o limite inicial: '))
lf = int(input('Digite o limite final: '))
for i in range(li+1,lf):
    if i % 3 == 0:
        print(i)