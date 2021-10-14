import json

def write_num():
    fn='fav_number.json'

    n = input("Digite seu numero favorito")
    with open(fn, 'w') as f:
        json.dump(n, f)


write_num()

def read_num():
    fn='fav_number.json'

    with open(fn) as f:
        num = json.load(f)
    
    print("Eu sei seu numero favorito, é "+num)

read_num()