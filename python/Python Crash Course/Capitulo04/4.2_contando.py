"""
lista = []

for i in range(1, 1000001):
    lista.append(i)

#print(lista)

print( min(lista) )
print( max(lista) )
print( sum(lista) )
"""

'''
for i in range(1, 20, 2):
    print( i)

'''

'''
for i in range(3, 31, 3):
    print( i)
'''

for i in range(1, 11):
    print(i ** 3)

lista = [ i**3 for i in range( 1, 11 ) ]
print(lista)