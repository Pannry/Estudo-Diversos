'''

lista = [i for i in range(1,100)]
print(lista)

print(lista[:3])

tamanho = len(lista)/2
tamanho = round(tamanho)

print( lista[ tamanho-1:tamanho+2 ] )

print(lista[-3:])


'''

my_pizzas = ["Queijo", "Carne", "Frango"]

friend_pizzas = my_pizzas[:]

print(my_pizzas)
print(friend_pizzas)

my_pizzas.append("Morango")
friend_pizzas.append("Chocolate")

print(my_pizzas)
print(friend_pizzas)
