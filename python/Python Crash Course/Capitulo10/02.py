#10.3
'''
file = 'guests.txt'

name = input('Digite seu nome: ')

with open(file, 'w') as f:
    f.write(name+'\n')

with open(file, 'r') as f:
    lines = f.read()
    print("### Lendo Arquivo ###")
    print(lines)
'''
#10.4
'''
file = 'book_guests.txt'

a = True
while a == True:
    name = input('Digite seu nome (exit p/ sair): ')
    

    if name != 'exit':
        print('Bem vindo, '+name)
        with open(file, 'a') as f:
            f.write(name+'\n')
    else:
        a = False
'''