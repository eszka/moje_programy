__author__ = 'Agnieszka'

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def eat(self, food):
        if(food == 'apple'):
             self.health -= 100
        elif (food == 'ham'):
            self.health += 20

#             tu bob to objekt






