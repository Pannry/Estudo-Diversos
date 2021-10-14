t = list( map( float, input().split() ) )

if t[0] + t[1] > t[2] and t[0]+t[2] > t[1] and t[1]+t[2]>t[0]:
    a = t[0]+t[1]+t[2]
    print( "Perimetro = "+str(a) )
else:
    a = ( (t[0]+t[1])*t[2] )/2
    print("Area = "+str(a))