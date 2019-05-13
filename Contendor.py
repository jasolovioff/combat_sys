import random


class Contendor:

    name = ""
    hp = 10
    armorClass = 10
    thac0 = 20
    health = 10
    weaponDamage = 6

    def __init__(self, name):
        self.name = name

    def isAlive(self):
        alive = False
        if self.health > 0:
            alive = True
        return alive

    def recieveDamage(self, damage):
        self.health = self.health - damage

    def calcDamage(self):
        return random.randint(1, self.weaponDamage)

    def hitEnemy(self, enemy):
        if self.isAlive():
            hitRoll = random.randint(1, 20)

            if hitRoll > self.thac0 - enemy.armorClass:
                enemy.recieveDamage(self.calcDamage())

