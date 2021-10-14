t = list( map( float, input().split() ) )
t.sort(reverse=True)

def tri():

    if t[0]**2 == t[1]**2 + t[2]**2:
        print("TRIANGULO RETANGULO")
    if t[0]**2 > t[1]**2 + t[2]**2:
        print("TRIANGULO OBTUSANGULO")
    if t[0]**2 < t[1]**2 + t[2]**2:
        print("TRIANGULO ACUTANGULO")
    if t[0] == t[1] == t[2]:
        print("TRIANGULO EQUILATERO")
    if t[0] == t[1] != t[2] or t[0] == t[2] != t[1] or t[1] == t[2] != t[0]:
        print("TRIANGULO ISOSCELES")

if t[0] >= t[1]+t[2]:
    print("NAO FORMA TRIANGULO")
else:
    tri()
