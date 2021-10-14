entradas = list( map( int, input().split() ) )

vetor = entradas [:]
vetor.sort()

for v in vetor:
    print(v)

print("")

for entrada in entradas:
    print(entrada)
