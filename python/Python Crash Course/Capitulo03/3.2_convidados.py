names = ['adam', 'brian', 'carmus', 'darius', 'eloin']

a = ("Você, "+ names[0].title() + ", está convidado para agir hoje para a conquista do mundo!!")

def message( pos ):
    return ("Você, "+ names[pos].title() + ", está convidado para agir hoje para a conquista do mundo!!\n")
    

print( message(0) )
print( message(1) )
print( message(2) )
print( message(3) )
print( message(4) )

print("Infelizmente, "+ names[3].title() + ", não pode dominar o mundo hoje. =(\n")

names[3] = "Hector"

print( message(0) )
print( message(1) )
print( message(2) )
print( message(3) )
print( message(4) )

