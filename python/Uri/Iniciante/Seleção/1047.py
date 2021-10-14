t = list( map( int, input().split() ) )

a = 24 - t[0] + t[2]
b = 60 - t[1] + t[3]

if(a >24):
    a = a % 24
if(b > 59):
    b = b % 60
if(t[1] > t[3]):
    a -= 1

print("O JOGO DUROU "+str(a)+" HORA(S) E "+str(b)+" MINUTO(S)")