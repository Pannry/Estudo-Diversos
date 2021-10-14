alien_0 = {}

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['color'] = 'yellow'

print(alien_0)
'''
del alien_0['points']

print(alien_0)
'''

print('\n'+ str( alien_0.items() ) )

#se eu passar dois parametros para o 'for', 
#preciso usar o metodo .items()

for k, v in alien_0.items():
    print( "\nKey: "+ k )
    print( "value: "+ str(v) )

#colocando em ordem
#sorted( dict_value ) organiza em ordem alfabetica
#.key() retorna o primeiro valor do dicionario
#.values() retorna o segundo valor do dicionario

favNumbers = {
    'Elisa' : '8',
    'Adam': '5',
    'Daniel': '5',
    'Brian': '1',
    'Carlos': '8',
}

for k in sorted( favNumbers.keys() ) :
    print( "\nKeys: "+ k )

for v in sorted( favNumbers.values() ):
    print( str('\nValues: '+ v) )

#set( dict_value ) mostra apenas valores unicos, nao repetidos

for v in set( favNumbers.values() ):
    print( str('\nNumbers: '+ v) )