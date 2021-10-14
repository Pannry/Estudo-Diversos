Winterwing = {
    'Name' : 'Ratheas',
    'race' : 'Night Elf',
}
Shortwrench = {
    'Name' : 'Glinklink',
    'race' : 'Gnome',
}
Bonegriever = {
    'Name' : 'Cluny',
    'race' : 'Forsaken',
}
Raindraft = {
    'Name' : 'Sikmpi',
    'race' : 'Tauren',
}

races = []
races.append(Winterwing)
races.append(Shortwrench)
races.append(Bonegriever)
races.append(Raindraft)

for race in races:
    print( "O "+race['Name']+'é da raça '+race['race']+".\n" )