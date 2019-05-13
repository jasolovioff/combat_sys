from Contendor import Contendor
import random

contendorA = Contendor("Abarradás")

contendorB = Contendor("Boltor")

while contendorA.health > 0 and contendorB.health > 0:
    contendorA.hitEnemy(contendorB)
    contendorB.hitEnemy(contendorA)
    print(str(contendorA.health) + " | " + str(contendorB.health))
