import math


class Point():
    '''Classe que guarda a posição dos pontos'''
    def __init__(self, x=0, y=0):
        '''
        Inicia a classe Point, definindo a posição inicial.
        Se não forem passados parametros, inicia na origem.
        '''
        self.move(x, y)

    def move(self, x, y):
        '''Determina a posição passada por parametro do ponto'''
        self.x = x
        self.y = y

    def reset(self):
        '''Move o ponto para a origem'''
        self.move(0, 0)

    def calculate_distance(self, other_point):
        '''Calcula a distancia do ponto da classe com outro ponto passado por parametro.'''
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def print(self):
        '''printa a posição do ponto'''
        print('x = '+str(self.x)+' y = '+str(self.y))

if __name__== '__main__':
    Point()

p1 = Point(y=6)
p2 = Point(3, 4)

p1.print()
p2.print()

print(str(p1.calculate_distance(p2))+", "+str(p2.calculate_distance(p1)))

# help(Point())