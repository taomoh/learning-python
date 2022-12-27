import random

class Dice(object):

    def __init__(self, sides):
        self.sides = sides
        
    def roll(self):
        return random.randint(1, self.sides)


d1 = Dice(6)
print(d1.roll())
print(d1.roll())
print(d1.roll())

print("")

d2 = Dice(10)
print(d2.roll())
print(d2.roll())
print(d2.roll())
print(d2.roll())
print(d2.roll())
