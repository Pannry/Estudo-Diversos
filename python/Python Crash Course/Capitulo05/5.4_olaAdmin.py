"""
names = ['adam', 'brian', 'carmus', 'darius', 'admin']

for name in names:
    if name == "admin":
        print("Ola, Gostaria de ver um relatório de status?")
    else:
        print("Ola, bem vindo novamente.")

"""

users = ["aaa", "bbb", "ccc"]
tam = len(users) 

for i in range(0, tam):
    if users != []:
        users.pop()
    
    if users == []:
        print("lista vazia")