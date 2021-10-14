
a = input().split()
a = list( map (int, a) )

if a[1] > a[2] 	and a[3] > a[0]:
    b = True
else:
    b = False

if ( a[2]+a[3] ) > ( a[0]+a[1] ):
    c = True
else:
    c = False

if a[2] > 0 and a[3] > 0:
    d = True
else:
    d = False

if a[0] % 2 == 0:
    e = True
else:
    e = False

if  b and c and d and e:
	print("Valores aceitos")
else:
	print("Valores nao aceitos") 