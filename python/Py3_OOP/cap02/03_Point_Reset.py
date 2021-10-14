class Point():

    def reset(self):
        self.x = 0
        self.y = 0

p = Point()

p.x = 3
p.y = 4

p.reset()

print(p.x, p.y)