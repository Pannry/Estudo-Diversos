class Restaurant():

    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        print("O "+self.restaurant_name+" oferece comidas do tipo "+self.cousine_type)

    def open_restaurant(self):
        print("Restaurante aberto!")


r = Restaurant('Galo', 'italiano')

r.describe_restaurant()
r.open_restaurant()