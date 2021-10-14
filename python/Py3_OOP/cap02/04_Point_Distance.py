import math


class Point():
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def print(self):
        print('x = '+str(self.x)+' y = '+str(self.y))


p1 = Point()
p2 = Point()

p1.reset()

p2.move(3, 6)
p1.move(2, 4)

p1.print()
p2.print()

print(p1.calculate_distance(p2))
print(p2.calculate_distance(p1))
