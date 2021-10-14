places = {
    'Winterwing' : ['Night Elf', 'Ratheas'],
    'Shortwrench' : ['Glinklink','Gnome', 'Shortwrench'],
    'Bonegriever' : ['Cluny', 'Forsaken'],
    'Raindraft' : ['Sikmpi'],
}

for k, vs in places.items():
    print("\nFavorite place of "+ k.title() +" is: ")
    for v in vs:
        print('\t'+v.title())