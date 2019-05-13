from Contendor import Contendor
import random

contendorA = Contendor("Abarradás")

contendorB = Contendor("Boltor")


def hitEachOther(contendor1, contendor2):
    isHit = False
    hitRoll = random.randint(1, 20)

    if hitRoll > contendor1.thac0 - contendor2.armorClass:
        isHit = True

    if isHit:
        damageRoll = random.randint(1, 6)
        contendor2.damage(damageRoll)


while contendorB.health > 0:
    hitEachOther(contendorA, contendorB)
    print(contendorB.health)
