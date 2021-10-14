t = list( map( int, input().split() ) )

a = 24 - t[0] + t[1]

if(a >24):
    a = a % 24

print("O JOGO DUROU "+str(a)+" HORA(S)")