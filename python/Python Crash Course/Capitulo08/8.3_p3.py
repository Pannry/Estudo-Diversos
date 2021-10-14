"""
def city_country( places ):
    for ci, co in places.items():
        print(co+", "+ci)



places = {}

flag = True
##
while flag:
    print('\n Digite "q" para sair')
    city = input("Nome da cidade: ")
    country = input("Nome do país: ")

    if city != 'q' and country != 'q':
        places[country] = city
    else:
        flag = False
##

city_country( places )

"""

def make_album():
    
    flag = True
    album = {}

    while flag:
        print('\n Digite "q" para sair')
        title = input("Titulo: ")
        description = input("Descrição: ")

        if title != 'q' and description != 'q':
            album[title] = description
        else:
            flag = False
    
    return album



#Criacao dos 3 albuns
'''
se true:
    criar album
senao
    printar todos albuns
'''
print("\n++Preenchendo album++")
album1 = make_album()
print("\n++Preenchendo album++")
album2 = make_album()
print("\n++Preenchendo album++")
album3 = make_album()

print(album1)
print(album2)
print(album3)