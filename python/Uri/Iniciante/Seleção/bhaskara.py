from math import sqrt

def delta(vet):
    d = ( vet[1]*vet[1] ) - ( 4 * vet[0] * vet[2] )
    return sqrt(d)

def caso1():
    R1 = ( -a[1] + D ) / (2*a[0])
    R2 = ( -a[1] - D ) / (2*a[0])

    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)

def caso2():
    R1 = ( -a[1] + D ) / 2*a[0]

    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R1)

def casos():
    try:
        if D > 0:
            caso1()
        elif D == 0:
            caso2()
        else:
            print("Impossivel calcular")
    except ZeroDivisionError:
        print("Impossivel calcular")


a = list( map( float, input().split() ) )

try:
    D = delta(a)
except ValueError:
    print("Impossivel calcular")
else:
    casos()