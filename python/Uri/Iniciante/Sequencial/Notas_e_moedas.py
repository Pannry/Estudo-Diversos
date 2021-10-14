
def saida_notas(qtd, preço):
    print(str(qtd)+ " nota(s) de R$ "+str(preço)+".00")

def saida_moedas(qtd, preço):
    if preço == 1:
        print(str(qtd)+ " moeda(s) de R$ "+str(preço)+".00")
    else:    
        print(str(qtd)+ " moeda(s) de R$ "+"%.2f" %preço)

total = input()

t = float(total)
t+= 1e-9    #Linha de codigo nescessaria para o uri aceitar a submissao
            #nao me pergunte o porque....

valores = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for valor in valores:
    count = 0
    while t >= 0 and t >= valor:
        count += 1
        t = t - valor
    saida_notas(count, valor)

print("MOEDAS:")


valores = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
for valor in valores:
    count = 0
    while t >= 0 and t >= valor:
        count += 1
        t = t - valor
    saida_moedas(count, valor)