names = ['adam', 'brian', 'carmus', 'hector', 'eloin']

a = ("Você, "+ names[0].title() + ", está convidado para agir hoje para a conquista do mundo!!")

def message( pos ):
    return ("Você, "+ names[pos].title() + ", está convidado para agir hoje para a conquista do mundo!!\n")
    

print( message(0) )
print( message(1) )
print( message(2) )
print( message(3) )
print( message(4) )

print("Abriu vaga na pt para dominar o mundo!\n")

names.insert(0, "igor")
names.insert(3, "kraw")
names.append("Mardoc")

print( message(0) )
print( message(1) )
print( message(2) )
print( message(3) )
print( message(4) )
print( message(5) )
print( message(6) )
print( message(7) )