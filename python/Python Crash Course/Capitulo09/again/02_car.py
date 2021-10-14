class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) +' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("O carro andou " + str(self.odometer_reading) + " quilometros.")

    def update_odometer(self, mielage):
        if mielage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode diminuir o odometro")

my_new_car = Car('audi', 'a4', 2014)
print(my_new_car.get_descriptive_name())
