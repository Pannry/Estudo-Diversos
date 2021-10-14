import json


def remember_me():
    username = input("Qual o seu nome? ")

    fn = 'username.json'
    with open(fn, 'w') as f:
        json.dump(username, f)
        print("Nos nos lembraremos de vc quando voltar, "+username+"!")

def greet_user():
    filename='username.json'
    with open(filename) as f:
        username = json.load(f)
        print("Bem vindo de volta, "+username+"!")


remember_me()
greet_user()
