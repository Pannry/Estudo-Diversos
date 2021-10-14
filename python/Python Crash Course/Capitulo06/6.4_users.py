
user_01 = {
    'first_name': 'Pamela',
    'last_name' : 'Fowler',
    'age': 56 , 
    'city': 'Suncrest'
}
user_02 = {
    'first_name': 'Guy','last_name' : 'Nagel',
    'age':34, 
    'city': 'Tallmadge'
}
user_03 = {
    'first_name': 'Jennifer',
    'last_name' : 'Green',
    'age':49, 
    'city': 'San Francisco'
}

people = []
people.append(user_01)
people.append(user_02)
people.append(user_03)

for user in people:
    print('Nome: '+user['first_name'])
    print('Sobrenome: '+user['last_name'])
    print('Idade: '+ str( user['age'] ) )
    print('Cidade: '+user['city'])
    print('\n')