#ultima parte das questoes do cap 07

'''
sandwich_orders = ['Atum', 'Presunto', 'Queijo', "Misto", 'Carne', 'Frango']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Preparando seu sanduiche de "+sandwich)

    finished_sandwiches.append(sandwich)


print("Sanduiches Preparados: ")
for i in finished_sandwiches:
    print('\t'+i)

'''

'''
sandwich_orders = ['Pastrami','Atum', 'Presunto', 'Pastrami', 'Queijo', "Misto", 'Pastrami', 'Carne', 'Frango']
finished_sandwiches = []

print("Pastrami esta em falta!")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)

'''

personal_info = {}
flag1 = True


while flag1:

    name = input("Digite o seu nome: ")
    info = input("Digite o nome do local destino: ")

    personal_info[name] = info

    flag2 = input("Deseja continuar? (y,n)")
    if flag2 == 'n':
        flag1 = False

print('\n---Resultados---')
for i, j in personal_info.items():
    print('\nO '+i+' deseja ir para '+j+'.')
    