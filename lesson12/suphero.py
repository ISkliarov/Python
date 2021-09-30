# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------
from hero import *

class SuperHero(Hero):
    """ Class to Create Super Hero """
    def __init__(self, name, level, race, magic_lavel):
        """ Initiate our Super Hero """
        super().__init__(name, level, race)
        self.magic_lavel = magic_lavel
        self.__magic = 100

    def make_magic(self):
        self.__magic = self.__magic - 10

    def show_hero(self):
        """ Print all parameters of tyis Hero """
        description = (self.name + " " + "Level is: " + str(self.level) + " " + "Race is: " + self.race + " " + "Health: " + str(self.health) + " Magik is: " + str(self.__magic)).title()
        print(description)