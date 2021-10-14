v = input()
tempo = int(v)

ano = tempo / 356
ano = int(ano)

print(str(ano) +" ano(s)")
tempo = tempo - ano*365

meses = tempo / 30
meses = int(meses)

print(str(meses)+" mes(es)")
tempo = tempo - meses*30

print(str(tempo) + " dia(s)")