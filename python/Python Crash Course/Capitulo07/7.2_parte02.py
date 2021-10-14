'''#ingredients = ['Chocolate', 'Limao', 'Tomate', 'Cebola', 'Ovo', 'Queijo']
ingredients = []
message = 'Quais ingredientes vc deseja: \n?-'

ing = ''

active = True

while active:
    ing = input(message)
    if ing == 'quit':
        active = False
    else:
        ingredients.append(ing)


for i in ingredients:
    print("Adicionando "+i+" na pizza!")

'''

'''
prompt = 'Qual a sua idade? \n?-'
message = "O ingresso custa "

age = input(prompt)
age = int(age)

if age <= 3:
    print(message+ "0 Dolares")
elif  age <= 12:
    print(message+ "10 Dolares")
else:
    print(message+ "15 Dolares")

'''
'''
#ingredients = ['Chocolate', 'Limao', 'Tomate', 'Cebola', 'Ovo', 'Queijo']
ingredients = []
message = 'Quais ingredientes vc deseja: \n?-'

ing = ''

active = True

while active:
    ing = input(message)
    if ing == 'quit':
        break
    else:
        ingredients.append(ing)


for i in ingredients:
    print("Adicionando "+i+" na pizza!")
'''