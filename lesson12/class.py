# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

from suphero import *
from hero import *

myhero = Hero("Bestiya", 3, "Bests")
mysuperhero = SuperHero("Moisey", 10, "Human", 5)

myhero.show_hero()

mysuperhero.show_hero()

mysuperhero.make_magic()

mysuperhero.show_hero()

mysuperhero.make_magic()
mysuperhero.make_magic()

mysuperhero.magic = 10

mysuperhero.show_hero()