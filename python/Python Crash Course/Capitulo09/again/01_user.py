class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describer_user(self):
        print("Nome: "+self.first_name.title()+"\nSobrenome: "+self.last_name.title())

    def greet_user(self):
        print("Bem vindo "+self.first_name.title()+"!")


user1 = User("Thales", "diniz")

user1.describer_user()
user1.greet_user()
