
def saida(qtd, preço):
    print(str(qtd)+ " nota(s) de R$ "+str(preço)+",00")

total = input()

print(total)

t = int(total)

valores = [100, 50, 20, 10, 5, 2, 1]

for valor in valores:
    count = 0
    while t >= 0 and t >= valor:
        count += 1
        t = t - valor
    saida(count, valor)