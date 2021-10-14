entradas = list( map( int, input().split() ) )

if entradas[1] % entradas[0] == 0 or entradas[0] % entradas[1] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")