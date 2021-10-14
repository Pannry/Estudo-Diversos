'''class Restaurant():

    def __init__(self, restaurant_name, city_name):
        self.restaurant_name = restaurant_name
        self.city_name = city_name
        self.number_served = 0

    def describre_restaurant(self):
        print(self.restaurant_name+', '+self.city_name)
    
    def open_restaurant(self):
        print("O restaurante está aberto")

    def set_number_served(self, num):
        self.number_served += num
        print("Total de pessoas servidas: "+ str(self.number_served) )

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, city_name):
        super().__init__( restaurant_name, city_name )
        self.flavors = ['chocolate', 'morango', "abacaxi"]

    def Sabores(self):
        for flavor in self.flavors:
            print(flavor)

rest1 = Restaurant("Da casa", "Fortaleza")

rest1.describre_restaurant()
rest1.open_restaurant()
rest1.set_number_served(1)

rest1.set_number_served(3)

sorv = IceCreamStand("Do bairro", "Fortaleza")
sorv.Sabores()
'''
'''
miss_message = 'Nao informado.'
class User():
    miss_message = 'Nao informado.'
    def __init__(   self, first_name, last_name, 
                    age= miss_message, email= miss_message ):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempt = 0

    def describe_user(self):
        print("Nome Completo: "+self.first_name+' '+self.last_name)
        print("Idade: "+ str(self.age) )
        print("Email: "+ self.email+"\n" )

    def greet_user(self):
        print("Seja bem vindo ao Sistema, "+self.last_name+"!")
    
    def login_attempts(self):
        self.login_attempt += 1
        print("Quantidade de tentativas: "+str( self.login_attempt ))

    def reset_login_attempts(self):
        self.login_attempt = 0
        print("Tentativas de login resetadas: "+ str( self.login_attempt )+"\n")
        

class Admin(User):
    miss_message = 'Nao informado.'
    def __init__(self, first_name, last_name, 
                    age= miss_message, email= miss_message):
        super().__init__( first_name, last_name, 
                    age= miss_message, email= miss_message)
        
        self.age = age
        self.email = email

        self.privileges = ['can add posts','can delete posts','can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
    
    

user01 = User('John', 'May', 53, 'JohnCMay@armyspy.com')

user01.describe_user()
user01.login_attempts()
user01.login_attempts()
user01.reset_login_attempts()

admin1 = Admin("Ivan", 'Karov', 36, "IvanKarov@armyspy.com")

admin1.describe_user()
admin1.show_privileges()

'''

