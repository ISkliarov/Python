# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

from hero import *

myhero1 = Hero("Vurdalac", 5, "Ork")
myhero2 = Hero("Alexander", 4, "Human")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.set_health(70)
myhero1.show_hero()