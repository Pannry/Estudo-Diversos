users = [ "Adam", "Brian", "Cardo", "Davi", "Elias" ]

new_users = ["Caio","davi","JamES"]
i = True

for n in new_users:
    for nomes in users:
        if ( n.lower() == nomes.lower() ):
            print( n.title() + "\t: nome não disponivel" )
            i = False
    if (i == True):
        print( n.title() + "\t: nome disponivel" )
    elif ( i == False):
        i = True